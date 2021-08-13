#!/usr/bin/python3
#---------------------
#ScriptName : login.py
#---------------------
#
#FROM: https://stackoverflow.com/questions/17540971/how-to-use-selenium-with-python

# Finding xpath of any object..
#
#    USE IDE to find xpath of object / element
#    And use find_element_by_xpath().click()
#
# There is an another way that you can find xpath of any object -
#
#    Install Firebug and Firepath addons in firefox
#    Open URL in Firefox
#    Press F12 to open Firepath developer instance
#    Select Firepath in below browser pane and chose select by "xpath"
#    Move cursor of the mouse to element on webpage
#    in the xpath textbox you will get xpath of an object/element.
#    Copy Paste xpath to the script.
#
# You can also use css_selector instead of xpath. Firepath will also
# capture css_selector if tou move cursor to the object. You will have to
# use then - find_element_by_css_selector(css_selector) 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "http://10.0.0.1/"
username = "admin"
password = "The-Ark-1793"

xpaths = { 'usernameTxtBox' : "//input[@name='username']",
           'passwordTxtBox' : "//input[@name='password']",
           'submitButton' :   "//input[@name='login']"
         }

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()

#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()
