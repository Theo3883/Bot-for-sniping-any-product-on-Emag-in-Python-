from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import subprocess
import os

with open('accountdetails.txt', 'r') as file:
    max_price = file.readlines()
with open('captchaAPI.txt', 'r') as file:
    captcha = file.readlines()

'''#adding captcha solver
options = webdriver.ChromeOptions()
options.add_extension('./captcha.crx')
driver = webdriver.Chrome(options=options)'''

options = webdriver.ChromeOptions()
options.add_argument("--remote-debugging-port=9222")
options.add_extension('./captcha.crx')

driver = webdriver.Chrome(options=options)
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])
key = driver.find_element(By.NAME, 'apiKey')
key.send_keys(captcha[0])
driver.find_element(By.ID, 'connect').click()
time.sleep(1)
driver.switch_to.alert.accept()
driver.switch_to.window(driver.window_handles[0])

#driver = webdriver.Chrome()
driver.get("https://auth.emag.ro/user/login")
driver.maximize_window()
email = driver.find_element(By.XPATH, '//*[@id="user_login_email"]')
email.send_keys(max_price[0])
random_wait_time = random.randrange(1, 2)
time.sleep(5)
action = ActionChains(driver)
action.send_keys(Keys.ESCAPE).perform()
driver.find_element(By.CLASS_NAME, 'captcha-solver-info').click()
time.sleep(40)

#enter password
password = driver.find_element(By.ID, 'user_register_password_first')
password.click()
password.send_keys(max_price[1])
password = driver.find_element(By.ID, 'user_register_password_second')
password.click()
password.send_keys(max_price[1])

#enter name
name = driver.find_element(By.ID, 'user_register_full_name')
name.click()
name.send_keys(max_price[2])

#agree to terms and continue
driver.execute_script("document.getElementById('user_register_agree_terms').click()")

#driver.find_element(By.ID, 'user_register_continue').click()
#time.sleep(10)  
driver.find_element(By.CLASS_NAME, 'captcha-solver-info').click()
time.sleep(40)
driver.find_element(By.LINK_TEXT, "Confirmă mai târziu").click()

#adress adding
driver.execute_script("document.getElementsByClassName('user-account-menu-delivery-addresses')[0].click()")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary.btn-link.underline.pad-sep-none.js-add-new-address.hidden-xs").click()
user = driver.find_element(By.ID, "user-name")
user.click()
user.send_keys(max_price[2])
phone = driver.find_element(By.ID, "user-phone")
phone.click()
phone.send_keys(max_price[3])

#select state
driver.find_element(By.CSS_SELECTOR, ".ph-widget.ph-select.form-control.js-modal-districts").click()
time.sleep(0.1)
value = max_price[4]
action = ActionChains(driver)
action.send_keys(value).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
time.sleep(0.5)

#select city
driver.find_element(By.CSS_SELECTOR, ".ph-widget.ph-select.form-control.js-modal-localities").click()
value = max_price[5]
action = ActionChains(driver)
action.send_keys(value).perform()
action.send_keys(Keys.ARROW_DOWN).perform()
action.send_keys(Keys.ENTER).perform()
time.sleep(0.5)

#enter street
street = driver.find_element(By.ID, "user-street")
street.click()
street.send_keys(max_price[6])

driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.js-save-changes.btn-save-change.btn-secondary").click()
time.sleep(0.5)

# Get the current working directory
current_directory = os.getcwd()
# Specify the command to run
command = ['python', os.path.join(current_directory, 'find.py')]
# Use subprocess to run the command
subprocess.run(command, check=True, text=True)
