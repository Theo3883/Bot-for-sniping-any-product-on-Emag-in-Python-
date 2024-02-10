from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import os
import subprocess

options = webdriver.ChromeOptions()
options.add_extension('./captcha.crx')
driver = webdriver.Chrome(options=options) 

driver.switch_to.window(driver.window_handles[0])
key = driver.find_element(By.NAME, 'apiKey')
key.send_keys('3ad413d9a8ba284ea5ce7ceb615a33a7')
driver.find_element(By.ID, 'connect').click()
time.sleep(2)
driver.switch_to.alert.accept()
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.get("https://auth.emag.ro/user/login")
time.sleep(60)