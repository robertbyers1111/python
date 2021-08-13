#!/home/rmbjr60/TeamDrive/Python-2018/Selenium/bin/python

from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

input2_elem = browser.find_element_by_css_selector(input2_css_locator)
button4_elem = browser.find_elelment_by_xpath(button4_xpath_locator)

input2_elem.send_keys("Test Text")
button4_elem.click()

sleep(15)
browser.close()

