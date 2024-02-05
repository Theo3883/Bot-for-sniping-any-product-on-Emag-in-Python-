from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

with open('accountdetails.txt', 'r') as file:
    max_price = file.readlines()

driver = webdriver.Chrome()
driver.get("https://auth.emag.ro/user/login")
driver.maximize_window()
email = driver.find_element(By.XPATH, '//*[@id="user_login_email"]')
email.send_keys(max_price[0])
random_wait_time = random.randrange(1, 2)
time.sleep(5)
#driver.find_element(By.CLASS_NAME, 'captcha-solver-info').click()
#print(random_wait_time)
#time.sleep(random_wait_time)
#email = driver.find_element(By.ID, 'user_login_continue')
#email.click()
time.sleep(10)

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

driver.find_element(By.ID, 'user_register_continue').click()
time.sleep(10)  #add captcha solver here 

driver.find_element(By.LINK_TEXT, "Confirmă mai târziu").click()
time.sleep(10)

time.sleep(30)
#adress adding
driver.execute_script("document.getElementsByClassName('user-account-menu-delivery-addresses')[0].click()")
driver.find_element(By.CSS_SELECTOR, ".btn.btn-secondary.btn-link.underline.pad-sep-none.js-add-new-address.hidden-xs").click()
user = driver.find_element(By.ID, "user-name")
user.click()
user.send_keys(max_price[2])
phone = driver.find_element(By.ID, "user-phone")
phone.click()
phone.send_keys(max_price[3])
driver.find_element(By.CSS_SELECTOR, ".ph-widget.ph-select.form-control.js-modal-districts").click()
time.sleep(2)

state_element = driver.find_element(By.NAME, 'district_id')
state = Select(state_element)
state.select_by_value('849')
time.sleep(10)