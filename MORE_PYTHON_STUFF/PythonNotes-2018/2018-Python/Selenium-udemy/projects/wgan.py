#!/home/rmbjr60/2018-Python/Selenium-udemy/p352/bin/python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://player.listenlive.co/41691")
playButton = browser.find_element_by_css_selector("a[id='playButton']")
playButton.click()

# NOTE: to record this stream, this is a start..

# sox -b 32 -e unsigned-integer -r 96k -c 2 -d --clobber --buffer $((96000*2*10)) /tmp/soxrecording.ogg trim 0 10

#.. but the sound quality sucks. Need to figure that out.
