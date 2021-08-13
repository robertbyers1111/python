#!/usr/bin/python3

#FROM: https://gist.github.com/hugs/830011

# To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver

#zz# # iPhone
#zz# driver = webdriver.Remote(browser_name="iphone", command_executor='http://172.24.101.36:3001/hub')
#zz# 
#zz# # Android
#zz# driver = webdriver.Remote(browser_name="android", command_executor='http://127.0.0.1:8080/hub')
#zz# 

# Firefox 
driver = webdriver.Firefox()

# Google Chrome 
# driver = webdriver.Chrome()

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('http://codepad.org')

# Select the Python language option
python_link = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
python_link.click()

# Enter some text!
text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print('Hello,' + ' World!')")

# Submit the form!
#<input type="submit" name="submit" value="Submit">
submit_button = driver.find_element_by_name('submit')
submit_button.click()

# Make this an actual test. Isn't Python beautiful?
assert "Hello, World!" in driver.get_page_source()

# Close the browser!
driver.quit()

