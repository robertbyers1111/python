#!/home/rmbjr60/TeamDrive/Python-2018/Selenium/bin/python

from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.google.com/")
search_field = browser.find_element_by_css_selector("input[name='q']")
search_field.send_keys("python automation with selenium")

# Used this instead of click (see note below)
search_field.send_keys(webdriver.common.keys.Keys.RETURN)

# Clicking on search button failed with: 'Other element would receive the click'
#
#   search_btn = browser.find_element_by_css_selector("input[name='btnK']")
#   search_btn.click()

sleep(15)
browser.close()

