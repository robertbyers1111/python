#!/home/rmbjr60/TeamDrive/Python-2018/Selenium/bin/python

from time import sleep
from selenium import webdriver

theUrl="https://techstepacademy.com/trial-of-the-stones"


browser = webdriver.Chrome()
browser.get(theUrl)

# Riddle of stone

r1Answer='rock'

r1Input_elem = browser.find_element_by_css_selector(
  "input[name='r1Input']"
)

r1Btn_elem = browser.find_element_by_xpath(
  "//button[@id='r1Btn']"
)

r1Input_elem.send_keys(r1Answer)
r1Btn_elem.click()

password_data=browser.find_element_by_css_selector(
  "div#passwordBanner h4"
)

password = password_data.text

print()
print('password data:',password_data)
print('password:',password)

# Riddle of secret

r2Input_elem = browser.find_element_by_css_selector(
  "input[name='r2Input']"
)

r2Btn_elem = browser.find_element_by_xpath(
  "//button[@id='r2Butn']"
)

r2Input_elem.send_keys(password)
r2Btn_elem.click()

# The Two Merchants

merchA_wealth_xpath_locator = "//h2/../div/span/b/../../p[text()='3000']"
merchA_name_xpath_locator = "//h2/../div/span/b/../../p[text()='3000'] /../span"

merchA_name_element = browser.find_element_by_xpath(merchA_name_xpath_locator)
merchA_name = merchA_name_element.text

merchA_wealth_element = browser.find_element_by_xpath(merchA_wealth_xpath_locator)
merchA_wealth = merchA_wealth_element.text

print()
print('merchA_name_element:',merchA_name_element)
print('merchA_name:',merchA_name)
print()
print('merchA_wealth_element:',merchA_wealth_element)
print('merchA_wealth:',merchA_wealth)

richest_input_css_locator = "input[name='r3Input']"
richest_input_element = browser.find_element_by_css_selector(richest_input_css_locator)
richest_button_css_locator = "button[id='r3Butn']"
richest_button_element = browser.find_element_by_css_selector(richest_button_css_locator)

richest_input_element.send_keys(merchA_name)
richest_button_element.click()

print()
print('richest_input_element:',richest_input_element)
print('richest_button_element:',richest_button_element)

# Check results..

checkResults_button_css_locator = "button[name='checkButn']"
checkResults_button_element = browser.find_element_by_css_selector(checkResults_button_css_locator)
checkResults_button_element.click()

success_css_locator = "div#trialCompleteBanner h4"
success_element = browser.find_element_by_css_selector(success_css_locator)
success_text = success_element.text

print()
print('success_text:',success_text)

assert success_text == 'Trial Complete'

print()
print('SUCCESS!')

# That is all

browser.close()

