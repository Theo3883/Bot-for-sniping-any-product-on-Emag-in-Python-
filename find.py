from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import os
import subprocess

with open('accountdetails.txt', 'r') as file:
    details = file.readlines()
with open('captchaAPI.txt', 'r') as file:
    captcha = file.readlines()

#adding captcha solver
options = webdriver.ChromeOptions()
options.add_extension('./captcha.crx')
driver = webdriver.Chrome(options=options)  

driver.switch_to.window(driver.window_handles[0])
key = driver.find_element(By.NAME, 'apiKey')
key.send_keys(captcha[0])
driver.find_element(By.ID, 'connect').click()
time.sleep(1)
driver.switch_to.alert.accept()
driver.switch_to.window(driver.window_handles[0])

#login
driver.get("https://auth.emag.ro/user/login")
driver.maximize_window()
email = driver.find_element(By.XPATH, '//*[@id="user_login_email"]')
email.send_keys(details[0])
time.sleep(5)
action = ActionChains(driver)
action.send_keys(Keys.ESCAPE).perform()
driver.find_element(By.CLASS_NAME, 'captcha-solver-info').click()
time.sleep(40)

#email = driver.find_element(By.ID, 'user_login_continue')
#email.click()

password = driver.find_element(By.ID, 'user_login_password')
password.send_keys(details[1])
#password = driver.find_element(By.ID, 'user_login_continue')    
#password.click()
#time.sleep(15)
action = ActionChains(driver)
action.send_keys(Keys.ESCAPE).perform()
driver.find_element(By.CLASS_NAME, 'captcha-solver-info').click()

action.send_keys(Keys.ESCAPE).perform()
print("am dat escape")
time.sleep(40)

##get the max price
max_priceint = 0
for i in details[8].strip():  ##strip() for removing the newline character
    max_priceint = max_priceint*10 + int(i)

ok = 1
while(ok):

    #init the window
    driver.execute_script("window.open('', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.emag.ro/")
    driver.implicitly_wait(20)

    ## search for a product
    driver.find_element(By.ID, 'searchboxTrigger').click()
    driver.find_element(By.ID, 'searchboxTrigger').send_keys(details[7])
    driver.find_element(By.ID, 'searchboxTrigger').submit()

    ##find the cheapest product
    driver.find_element(By.XPATH, '//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div[1]/div[5]/div/div/div[2]/div[1]/button/span[2]').click()
    cheapest = driver.find_element(By.XPATH, '//*[@id="main-container"]/section[1]/div/div[3]/div[2]/div[1]/div[5]/div/div/div[2]/div[1]/div/ul/li[3]/a')
    cheapest.click()
    driver.implicitly_wait(20)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'card-v2-thumb-inner').click()

    ##get the price
    price_element = driver.find_element(By.XPATH, '//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div/div/div[1]/p[2]')
    price = price_element.text
    priceint = 0
    i=0
    while price[i] != ",":
        priceint = priceint*10 + int(price[i])
        i += 1
    if(priceint < max_priceint):
        ok = 0
        
        ##add to cart
        add_to_cart = driver.find_element(By.CSS_SELECTOR, '.em.em-cart_fill.gtm_680klw') #pc
        add_to_cart.click()

        random_wait_time = random.randrange(1, 2)
        print(random_wait_time)
        time.sleep(random_wait_time)

        #view cart
        view_cart = driver.find_element(By.LINK_TEXT, 'Vezi detalii cos')
        view_cart.click()
        driver.implicitly_wait(10)

        #continue to checkout
        random_wait_time = random.randrange(1, 2)
        print(random_wait_time)
        time.sleep(random_wait_time)
        continuecart = driver.find_element(By.LINK_TEXT, 'Continua')
        continuecart.click()
        driver.implicitly_wait(10)
        random_wait_time = random.randrange(1, 2)
        print(random_wait_time)
        time.sleep(random_wait_time)

        #checkout courier and numerar
        courier = driver.find_element(By.ID, 'courierTab')
        courier.click()
        numerar = driver.find_element(By.ID, 'paymentLinenumerar')
        numerar.click()
        driver.find_element(By.CSS_SELECTOR, '.emg-btn-icon.emg-btn-icon-large.gtm_stj738bt').click()
        break
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

time.sleep(60)
