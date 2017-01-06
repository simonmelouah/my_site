import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import string
from random import randint
from db_interaction import DbInteraction

connect = DbInteraction()

connect.

# Selenium test


url = 'https://simonmelouah.com/'

chromedriver = "/Users/simon/development/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)
driver.set_window_size(1900, 800)



cursor = """ "<div id='cursor' style='border-radius: 50%; background: red; width: 10px; height: 10px; position: fixed; top: 0; left: 0;'></div>" """
driver.execute_script("document.body.innerHTML = document.body.innerHTML + {0}".format(cursor))

for number in range(0, 600):
    x_postion = randint(0, 800)
    y_postion = randint(0, 800)
    move_cursor = """var element = document.getElementById('cursor'); element.style.position = "absolute"; element.style.left = {0}+'px'; element.style.top = {1}+'px';""".format(x_postion, y_postion)
    driver.execute_script(move_cursor)
    time.sleep(.25)

user_screen_width = "var user_screen_width = 1920;"
user_screen_height = " var user_screen_height = 403;"
screen_width = " var screen_width = window.innerWidth;"
screen_height = " var screen_height = window.innerHeight;"
percentage_width = " var percentage_width = screen_width / user_screen_width;"
percentage_height = " var percentage_height = screen_height / user_screen_height;"
relative_x_position = " var relative_x_position = percentage_width * 1483;"
relative_y_position = " var relative_y_position = percentage_height * 29;"
click = " document.elementFromPoint(relative_x_position, relative_y_position).click();"

driver.execute_script(user_screen_width + user_screen_height + screen_width + screen_height + percentage_width + percentage_height + relative_x_position + relative_y_position + click)
# driver.execute_script(" var user_screen_width = 1920 var w = .76 * window.innerWidth; var h = 29 * window.innerHeight; document.elementFromPoint(1476, h).click();")
time.sleep(3)
# driver.close()
