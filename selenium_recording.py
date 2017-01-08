import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import string
from random import randint
from db_interaction import DbInteraction

connect = DbInteraction()
mouse_recordings = connect.get_mouse_recordings()
# Selenium test


url = 'https://simonmelouah.com/'

chromedriver = "/Users/simon 1/Development/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)

window_width = 0
window_height = 0

for mouse_recording in mouse_recordings:
    if window_width != mouse_recording.window_width or window_height != mouse_recording.window_height:
        window_width = mouse_recording.window_width
        window_height = mouse_recording.window_height
        driver.set_window_size(window_width, window_height)

    cursor = """ "<div id='cursor' style='border-radius: 50%; background: red; width: 10px; height: 10px; position: fixed; top: {0}; left: {1};'></div>" """.format(mouse_recording.y_position, mouse_recording.x_position)
    driver.execute_script("document.body.innerHTML = document.body.innerHTML + {0};".format(cursor))
    if mouse_recording.event_type == "move":
        event = """var element = document.getElementById('cursor'); element.style.position = "absolute"; element.style.left = {0}+'px'; element.style.top = {1}+'px';""".format(mouse_recording.x_position, mouse_recording.y_position)
    else:
        event = " document.elementFromPoint({0}, {1}).click();".format(mouse_recording.x_position, mouse_recording.y_position)
    driver.execute_script(event)
    time.sleep(.5)

driver.close()

# var cursor = document.getElementById('cursor'); if (!cursor) {