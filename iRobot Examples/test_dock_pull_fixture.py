# Copyright 2019-2021 iRobot Corporation (Unpublished). All Rights Reserved.

import pytest
import logging


class TestDockPullFixture:
    """
    Integration tests for the Dock Pull fixture to test SSH connection and local script logic

    """

    pytestmark = [pytest.mark.unit_dock_pull]

    def test_dock_pull_fixture(self, physical_test_fixtures, env_cfg):
        """
        Verify that we can successfully connect to the fixture, retract and extend the actuator,
        and correctly assert its position as well as the dock environment as it changes

        """
        original_dock_environment = env_cfg.docks
        # If theres no dock in the environment config, add a temporary one so we can test its removal and restoration
        if not env_cfg.docks:
            env_cfg.docks = ['temp_dock_type']
        try:
            # Check that dock type is set
            assert env_cfg.docks, logging.error("Dock is not set in environment config file")

            # Ensure that the dock pull fixture is set up correctly
            assert physical_test_fixtures.dock_pull_fixture, logging.error("Dock pull hostname not include for test,"
                                                                           " use --dock-pull-hostname CLI option")
            original_dock_environment = physical_test_fixtures.dock_pull_fixture._original_dock_environment
            assert original_dock_environment == env_cfg.docks

            # Block and power off the dock and ensure that the dock environment is now empty
            physical_test_fixtures.dock_pull_fixture.power_off_dock()
            physical_test_fixtures.dock_pull_fixture.block_dock()
            assert env_cfg.docks == [], logging.error("Expected dock to be removed from env_cfg, instead was %s",
                                                      env_cfg.docks)

            # Make dock available again, ensure that the dock environment is restored to its original value
            physical_test_fixtures.dock_pull_fixture.unblock_dock()
            physical_test_fixtures.dock_pull_fixture.power_on_dock()
            assert env_cfg.docks == original_dock_environment, logging.error("Expected env_cfg.docks to be restored to "
                                                                             "original value of %s, instead was %s",
                                                                             original_dock_environment, env_cfg.docks)
        finally:
            # If the test errors out early on, we want to make sure that the dock environment still gets restored
            if env_cfg.docks != original_dock_environment:
                env_cfg.docks = original_dock_environment.copy()
            # Restore env_cfg to empty if it was originally empty
            if env_cfg.docks == ['temp_dock_type']:
                env_cfg.docks = []
