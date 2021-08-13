# Copyright 2020 iRobot Corporation (Unpublished). All Rights Reserved.

import pytest
import logging
import time

from common.mission.Mission import Mission
from common.mission.PauseResumeMission import PauseResumeMission
from common.mission.RechargeMission import RechargeMission
from common.mission.BinFullMission import BinFullMission
from common.mission.TankEmptyMission import TankEmptyMission
from common.mission_parameters.MissionParameters import MissionParameters
from common.mission_parameters.PauseResumeMissionParameters import PauseResumeMissionParameters
from common.mission_parameters.RechargeMissionParameters import RechargeMissionParameters
from common.mission_parameters.BinFullMissionParameters import BinFullMissionParameters
from common.mission_parameters.TankEmptyMissionParameters import TankEmptyMissionParameters

from utils.metrics import inline_mqtt_timer
from utils.post_processing import get_cleaning_passes

from utils.globals.robot_code_errors import NOT_READY_START_REFUSE_LOW_BATTERY


class TestPlatformBasicMissions:

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.stingray(category='experimental')
    @pytest.mark.production
    @pytest.mark.standard_dock
    def test_27789(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-27789: Basic Mission: Mission Starts on Standard Dock
        This test case is designed to verify the robot will complete a cleaning mission when starting from a
        standard dock.

        """
        mission_parameters = MissionParameters(clean_type='clean_all', start_dock='std', env_cfg=env_cfg)
        if mqtt_client.connection_type == 'remote':
            evaluators.toggle_evaluator('mission_timeline', 'assert', mission_parameters=mission_parameters,
                                        is_cloud_console_available=False, dock_type='std',
                                        original_cleaning_passes=get_cleaning_passes(mqtt_client))
        clean_all_mission = Mission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                    evaluators=evaluators)
        clean_all_mission.run_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.experimental
    @pytest.mark.sanmarino
    @pytest.mark.stingray
    def test_26497(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-26497: Basic Mission: Pause-Resume and Paused 90-Minute Timeout
        This tests the robot cancels a mission if it is paused for more than 90 minutes. An abort timeout override is
        acceptable for this test case. To change the timeout, send "abort_mission_time_min X" in Nav Roboscope where X
        is the desired timeout.

        """
        mission_parameters = PauseResumeMissionParameters(clean_type='clean_all', start_dock='any', env_cfg=env_cfg,
                                                          charge_resume_timeout_min=1, abort_mission_timeout_min=2,
                                                          wait_condition=("time_delay", 2))
        pause_resume_mission = PauseResumeMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                                  evaluators=evaluators)
        building_blocks = pause_resume_mission.building_blocks

        pause_resume_mission.pre_mission()
        pause_resume_mission.initiate_mission()

        building_blocks.wait_until_injection_condition_is_met()
        building_blocks.pause_then_resume()

        building_blocks.wait_until_condition('time_delay', 2)
        mqtt_client.pause()

        timed_wait_until_state_is = inline_mqtt_timer(mqtt_client.wait_until_state_is)
        time_before_timeout = timed_wait_until_state_is("none", "stop", timeout_secs=180)
        expected_time_before_timeout = 120 - 5  # 2 minutes minus the delay in pause()
        logging.info('Robot took [%d] seconds before timing out mission and cancelling mission', time_before_timeout)

        assert abs(time_before_timeout - expected_time_before_timeout) < 5, \
            logging.error('Expected robot to cancel mission in [%d] seconds, took [%d] instead, tolerance '
                          '[%d] seconds', expected_time_before_timeout, time_before_timeout, 5)
        
        building_blocks.send_robot_back_to_dock()
        pause_resume_mission.post_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.sanmarino
    @pytest.mark.experimental
    def test_29099(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-29099: Basic Mission: low mission start
        This test that the robot will start a full clean, spot clean, or a docking mission when the battery is at a
        minimum level.

        """
        mission_parameters = MissionParameters(clean_type='clean_all', start_dock='any', env_cfg=env_cfg,
                                               test_truncation_timeout_min=2)
        clean_all_mission = Mission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                    evaluators=evaluators)
        building_blocks = clean_all_mission.building_blocks
       
        # Override pre_mission to ensure the robot starts this test with a battery of between 16 and 27%
        roboscope.bat_pct_override(20)

        clean_all_mission.pre_mission()
        clean_all_mission.initiate_mission()

        building_blocks.wait_until_condition('time_delay', 2)
        mqtt_client.stop()
        mqtt_client.wait_until_state_is("none", "stop", timeout_secs=60)

        mqtt_client.spot()
        mqtt_client.wait_until_not_stopped(timeout_secs=10)
        assert mqtt_client.check_cycle_phase("spot", "run"), \
            logging.error("Expected robot to start a spot mission but it did not")

        mqtt_client.stop()
        mqtt_client.wait_until_state_is("none", "stop", timeout_secs=60)

        mqtt_client.dock()
        mqtt_client.wait_until_docked(timeout_mins=10)

        clean_all_mission.post_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.sanmarino
    @pytest.mark.experimental
    def test_26498(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-26498: Basic Mission: Low Battery Behavior
        This test case is designed to verify that the robot will not start a Clean or Spot mission if the battery is too
        low. It is acceptable to force the low battery condition using Roboscope.

        """
        mission_parameters = RechargeMissionParameters(clean_type='clean_all', start_dock='off_any', env_cfg=env_cfg,
                                                       wait_condition=("time_delay", 2),
                                                       check_clean_on_low_battery=True)
        clean_all_mission = RechargeMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                            evaluators=evaluators)

        clean_all_mission.pre_mission()
        roboscope.bat_pct_override(12)

        # Modified version of check_clean_on_low_battery_upon_condition
        logging.info("Check that robot refuses clean if battery is low...")
        assert mqtt_client.get_not_ready_code() == NOT_READY_START_REFUSE_LOW_BATTERY, \
            logging.error("notReady code should indicate that robot is not ready to clean.")
        mqtt_client.clean(post_command_wait_seconds=15)
        assert mqtt_client.check_cycle_phase("none", "stop"), \
            logging.error("Expected robot to ignore clean command due to low battery but did not.")

        mqtt_client.spot()
        time.sleep(5)
        assert mqtt_client.check_cycle_phase("none", "stop"), \
            logging.error("Expected robot to ignore spot command due to low battery but did not.")

        mqtt_client.dock()
        mqtt_client.wait_until_docked(timeout_mins=10)

        assert mqtt_client.get_not_ready_code() == NOT_READY_START_REFUSE_LOW_BATTERY, \
            logging.error("notReady code should indicate that robot is not ready to clean.")
        mqtt_client.clean(post_command_wait_seconds=15)
        assert mqtt_client.check_cycle_phase("none", "charge"), \
            logging.error("Expected robot to ignore clean command due to low battery but did not.")

        mqtt_client.spot()
        time.sleep(5)
        assert mqtt_client.check_cycle_phase("none", "charge"), \
            logging.error("Expected robot to ignore spot command due to low battery but did not.")

        mqtt_client.dock()
        if 'auto' in env_cfg.docks:
            mqtt_client.wait_until_state_is('evac', 'evac', timeout_mins=1)
        mqtt_client.wait_until_state_is('none', 'charge', timeout_mins=1)

        roboscope.bat_pct_override(-1)

        clean_all_mission.post_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.production
    @pytest.mark.standard_dock
    @pytest.mark.sanmarino
    @pytest.mark.stingray(category='experimental')
    def test_26507(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-26507: Basic Mission: Mission Starts off Standard Dock
        This test case is designed to verify that the robot will complete a mission when it started off the dock in a
        test area where a standard dock is present.
        """
        mission_parameters = MissionParameters(clean_type='clean_all', start_dock='off_std', env_cfg=env_cfg)
        clean_all_mission = Mission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                    evaluators=evaluators)
        clean_all_mission.run_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.stingray
    @pytest.mark.experimental
    def test_26479(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-26479: Basic Mission: Bin-Full Pause with Standard Dock
        This test case is designed to verify the behavior of the robot when a bin-full is triggered and it returns to
        the dock.

        """
        mission_parameters = BinFullMissionParameters(clean_type='clean_all', start_dock='off_std', env_cfg=env_cfg,
                                                      wait_condition=("time_delay", 2), pause_cleaning_when_full=True,
                                                      clear_bin_override=False, physical_bin_full=False)
        clean_all_mission = BinFullMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                           evaluators=evaluators)
        clean_all_mission.run_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.production
    @pytest.mark.evac_dock
    def test_27658(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-27658: Basic Mission: Mission Starts on Auto-Evac Dock
        This test case is designed to verify that the robot will complete a mission when starting from an Auto-Evac
        dock.
        """
        mission_parameters = MissionParameters(clean_type='clean_all', start_dock='auto', env_cfg=env_cfg)
        clean_all_mission = Mission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                    evaluators=evaluators)
        clean_all_mission.run_mission()

    @pytest.mark.lewis
    @pytest.mark.soho
    @pytest.mark.production
    @pytest.mark.evac_dock
    def test_27659(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-27659: Basic Mission: Mission Starts off Auto-Evac Dock
        This test case is designed to verify that the robot will complete a mission when it started off the dock in a
        test area where an Auto-Evac dock is present.
        """
        mission_parameters = MissionParameters(clean_type='clean_all', start_dock='off_auto', env_cfg=env_cfg)
        clean_all_mission = Mission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                    evaluators=evaluators)
        clean_all_mission.run_mission()

    @pytest.mark.experimental
    @pytest.mark.sanmarino
    @pytest.mark.standard_dock
    @pytest.mark.wet_pad
    def test_27608(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-27608: Basic Mission: Mission Starts on Dock, Disposable Wet Pad
        This test case is designed to verify that the robot can complete a wet cleaning mission with a Disposable Wet
        Pad when starting from a standard dock.

        """
        mission_parameters = TankEmptyMissionParameters(clean_type='clean_all', start_dock='std', env_cfg=env_cfg,
                                                        wait_condition=("time_delay", 2),
                                                        pad_type='dispWet')
        clean_all_tank_empty_mission = TankEmptyMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                                        evaluators=evaluators)
        building_blocks = clean_all_tank_empty_mission.building_blocks

        clean_all_tank_empty_mission.pre_mission()
        clean_all_tank_empty_mission.initiate_mission()
        building_blocks.wait_until_injection_condition_is_met()
        building_blocks.wait_until_mission_ends_or_truncation_timeout_reached()
        clean_all_tank_empty_mission.post_mission()

    @pytest.mark.experimental
    @pytest.mark.sanmarino
    @pytest.mark.standard_dock
    @pytest.mark.wet_pad
    def test_27693(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-27693: Basic Mission: Mission Starts on Dock, Reusable Wet Pad
        This test case is designed to verify that the robot can complete a wet pad cleaning mission with a Reusable
        Wet Pad when starting from a standard dock.

        """
        mission_parameters = TankEmptyMissionParameters(clean_type='clean_all', start_dock='std', env_cfg=env_cfg,
                                                        wait_condition=("time_delay", 2),
                                                        pad_type='reusableWet')
        clean_all_tank_empty_mission = TankEmptyMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                                        evaluators=evaluators)
        building_blocks = clean_all_tank_empty_mission.building_blocks

        clean_all_tank_empty_mission.pre_mission()
        clean_all_tank_empty_mission.initiate_mission()
        building_blocks.wait_until_injection_condition_is_met()
        building_blocks.wait_until_mission_ends_or_truncation_timeout_reached()
        clean_all_tank_empty_mission.post_mission()

    @pytest.mark.experimental
    @pytest.mark.sanmarino
    @pytest.mark.standard_dock
    @pytest.mark.dry_pad
    def test_27694(self, mqtt_client, roboscope, env_cfg, evaluators):
        """
        TC-27694: Basic Mission: Mission Starts on Dock, Disposable Dry Pad
        This test case is designed to verify that the robot can complete a wet cleaning mission with a Disposable Dry
        Pad when starting from a standard dock.

        """
        mission_parameters = TankEmptyMissionParameters(clean_type='clean_all', start_dock='std', env_cfg=env_cfg,
                                                        wait_condition=("time_delay", 2),
                                                        pad_type='dispDry')
        clean_all_tank_empty_mission = TankEmptyMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                                        evaluators=evaluators)
        building_blocks = clean_all_tank_empty_mission.building_blocks

        clean_all_tank_empty_mission.pre_mission()
        clean_all_tank_empty_mission.initiate_mission()
        building_blocks.wait_until_injection_condition_is_met()
        building_blocks.wait_until_mission_ends_or_truncation_timeout_reached()
        clean_all_tank_empty_mission.post_mission()

    @pytest.mark.experimental
    @pytest.mark.sanmarino
    @pytest.mark.no_docks
    @pytest.mark.dry_pad
    def test_27695(self, mqtt_client, roboscope, env_cfg, evaluators, physical_test_fixtures):
        """
        TC-27695: Basic Mission: No Dock Mission, Reusable Dry Pad
        This test case is designed to verify that the robot can complete a wet cleaning mission with a Reusable Dry Pad
        when cleaning with an area with no dock.

        """
        mission_parameters = TankEmptyMissionParameters(clean_type='clean_all', start_dock='none', env_cfg=env_cfg,
                                                        wait_condition=("time_delay", 2),
                                                        pad_type='reusableDry')
        clean_all_tank_empty_mission = TankEmptyMission(mqtt_client, roboscope, mission_parameters, cloud_console=None,
                                                        evaluators=evaluators,
                                                        physical_test_fixtures=physical_test_fixtures)
        building_blocks = clean_all_tank_empty_mission.building_blocks

        clean_all_tank_empty_mission.pre_mission()
        clean_all_tank_empty_mission.initiate_mission()
        building_blocks.wait_until_injection_condition_is_met()
        building_blocks.wait_until_mission_ends_or_truncation_timeout_reached()
        clean_all_tank_empty_mission.post_mission()
