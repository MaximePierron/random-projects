from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import re
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


def buy_item():
    item_to_buy = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed) b")[-1]
    item_to_buy.click()


t_end = time.time() + 60 * 5
checking_time = int(time.time()) + 5

while time.time() < t_end:
    cookie.click()
    if int(time.time()) == checking_time:
        buy_item()
        checking_time += 5

cookies_per_minutes_line = driver.find_element(By.ID, "cps").text
cookies_per_minutes = re.findall(r'\d+\.?\d+', cookies_per_minutes_line)
print(cookies_per_minutes)
