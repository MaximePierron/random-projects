from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

load_dotenv()
messenger_email = os.environ["MESSENGER_EMAIL"]
messenger_password = os.environ["MESSENGER_PASSWORD"]

chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# LOGIN TO MESSENGER
driver.get("https://www.messenger.com/")
buttons_div = driver.find_element(By.CLASS_NAME, "_9xo5")
buttons = buttons_div.find_elements(By.TAG_NAME, "button")
buttons[1].click()
name_input = driver.find_element(By.NAME, "email")
name_input.send_keys(messenger_email)
password_input = driver.find_element(By.NAME, "pass")
password_input.send_keys(messenger_password)
login_div = driver.find_element(By.CLASS_NAME, "_9h74")
login_button = login_div.find_element(By.TAG_NAME, "button")
login_button.click()

# SCRAPE MESSAGES
