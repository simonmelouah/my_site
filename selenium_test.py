import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random, string


# Selenium test

get_environment = raw_input("Local or live? ")

if "local":
    url = 'http://localhost:5555/'
else:
    url = 'http://www.simonmelouah.com/'

get_username = raw_input("Enter username: ")
get_password = raw_input("Enter password: ")
random_string = ''.join(random.choice(string.lowercase) for i in range(10))

chromedriver = "/Users/simon 1/development/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()

def get_route_test(url, endpoint = None):
    if endpoint:
        driver.get(url + endpoint)
    else:
        driver.get(url)
    time.sleep(1)

def login_test(username_input, password_input):
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    submit = driver.find_element_by_name("submit")
    username.send_keys(username_input)
    password.send_keys(password_input)
    submit.click()
    time.sleep(1)
    try:
        error = driver.find_element_by_id("error")
    except:
        error = None

    if error:
        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        username.clear()
        password.clear()

def add_project_test():
    title = driver.find_element_by_id("title")
    category = driver.find_element_by_id("category")
    technology = driver.find_element_by_id("technology")
    new_technology = driver.find_element_by_id("other_technology")
    description = driver.find_element_by_id("description")
    url = driver.find_element_by_id("url")
    youtube = driver.find_element_by_id("youtube")
    submit = driver.find_element_by_name("submit")

    title.send_keys(random_string)
    category.send_keys("1")
    technology.send_keys("1")
    new_technology.send_keys(random_string)
    description.send_keys(random_string)
    url.send_keys(random_string)
    youtube.send_keys(random_string)
    submit.click()
    time.sleep(1)

def hover_check_test():
    element_to_hover_over = driver.find_element_by_class_name("hoverCheck")
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
    time.sleep(1)

def send_message_test():
    name = driver.find_element_by_id("name")
    email = driver.find_element_by_id("email")
    phone = driver.find_element_by_id("phone")
    message = driver.find_element_by_id("message")
    submit = driver.find_element_by_name("submit")

    name.send_keys(random_string)
    email.send_keys(random_string+ "@" + random_string)
    phone.send_keys(random_string)
    message.send_keys(random_string)
    submit.click()

get_route_test(url)
get_route_test(url, "about")
get_route_test(url, "software_portfolio")
get_route_test(url, "sports")
get_route_test(url, "add_project")
get_route_test(url, "admin")

login_test(get_username, random_string)
login_test(random_string, get_password)
login_test(get_username, get_password)

add_project_test()

hover_check_test()

get_route_test(url, "get_stats")

get_route_test(url, "contact")

send_message_test()
driver.close()
