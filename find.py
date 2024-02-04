from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import subprocess

#empty cart
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://auth.emag.ro/user/login")
email = driver.find_element(By.XPATH, '//*[@id="user_login_email"]')
email.send_keys("teosandu88@gmail.com")
random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)
email = driver.find_element(By.ID, 'user_login_continue')
email.click()
time.sleep(10)
random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)
password = driver.find_element(By.ID, 'user_login_password')
password.send_keys("gabiMARIANA2")
password = driver.find_element(By.ID, 'user_login_continue')    
password.click()
time.sleep(15)

driver.execute_script("window.open('', '_blank');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.emag.ro/")
driver.implicitly_wait(20)

##get the max price
max_priceint = 0
with open('price.txt', 'r') as file:
    max_price = file.readlines()
for i in max_price:
    max_priceint = max_priceint*10 + int(i)

#read product from file
with open('product.txt', 'r') as file:
    product = file.readlines()

## search for a product
driver.find_element(By.ID, 'searchboxTrigger').click()
driver.find_element(By.ID, 'searchboxTrigger').send_keys(product)
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
    ##add to cart
    ##add_to_cart = driver.find_element(By.XPATH, '//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form/div/div[3]/div[2]/div[1]/button') #mac
    add_to_cart = driver.find_element(By.XPATH, '//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form[1]/div[1]/div[3]/div[3]/div[1]/button') #laptop
    add_to_cart.click()

    random_wait_time = random.randrange(1, 2)
    print(random_wait_time)
    time.sleep(random_wait_time)

    view_cart = driver.find_element(By.LINK_TEXT, 'Vezi detalii cos')
    view_cart.click()
    driver.implicitly_wait(10)

    random_wait_time = random.randrange(1, 2)
    print(random_wait_time)
    time.sleep(random_wait_time)
    continuecart = driver.find_element(By.LINK_TEXT, 'Continua')
    continuecart.click()
    driver.implicitly_wait(10)
    random_wait_time = random.randrange(1, 2)
    print(random_wait_time)
    time.sleep(random_wait_time)

    '''email = driver.find_element(By.XPATH, '//*[@id="user_login_email"]')
    email.send_keys("teosandu88@gmail.com")
    random_wait_time = random.randrange(1, 2)
    print(random_wait_time)
    time.sleep(random_wait_time)
    email = driver.find_element(By.ID, 'user_login_continue')
    email.click()

    random_wait_time = random.randrange(1, 2)
    print(random_wait_time)
    time.sleep(random_wait_time)
    password = driver.find_element(By.ID, 'user_login_password')
    password.send_keys("gabiMARIANA2")
    password = driver.find_element(By.ID, 'user_login_continue')    
    password.click()
    random_wait_time = random.randrange(1, 2)
    print(random_wait_time)
    time.sleep(random_wait_time)'''

    courier = driver.find_element(By.ID, 'courierTab')
    courier.click()
    numerar = driver.find_element(By.ID, 'paymentLinenumerar')
    numerar.click()

time.sleep(5)
