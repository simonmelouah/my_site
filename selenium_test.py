import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Selenium test

# Sets up chrome driver (required for chrome launch)
# chromedriver = "/Users/Simon/development/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Firefox()
# browser = webdriver.Chrome(chromedriver)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
# browser = webdriver.Chrome(chromedriver)

# Tests all different route access to make sure login is required for all
browser.get('http://google.com')
# browser.get('http://localhost:5555/home')
# browser.get('http://localhost:5555/projects')
# browser.get('http://localhost:5555/update_voucher')
# browser.get('http://localhost:5555/display')
# browser.get('http://localhost:5555/add')
# browser.get('http://localhost:5555/display/purchases/GHCL0147768')
# browser.get('http://localhost:5555/validate')
# browser.get('http://localhost:5555/change_password')