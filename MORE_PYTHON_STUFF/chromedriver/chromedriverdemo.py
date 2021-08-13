#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver = "/opt/chromedriver/chromedriver"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
driver.get("https://www.google.com")
lucky_button = driver.find_element_by_css_selector("[name=btnI]")
lucky_button.click()
driver.get_screenshot_as_file("capture.png")
