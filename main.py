from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import random 
wd = webdriver.Chrome()
wd.maximize_window()
wd.get("https://www.emag.ro/placa-video-asus-dual-geforce-rtxtm-2060-oc-edition-evo-6gb-gddr6-192-bit-dual-rtx2060-o6g-evo/pd/DRWM68BBM/")
wd.implicitly_wait(10)
add_to_cart = wd.find_element(By.XPATH, '//*[@id="main-container"]/section[3]/div/div[1]/div[2]/div/div[2]/div[2]/form/div/div[3]/div[3]/div[1]/button')
add_to_cart.click()

random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)

view_cart = wd.find_element(By.LINK_TEXT, 'Vezi detalii cos')
view_cart.click()
wd.implicitly_wait(10)

random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)
continuecart = wd.find_element(By.LINK_TEXT, 'Continua')
continuecart.click()
wd.implicitly_wait(10)
random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)

email = wd.find_element(By.XPATH, '//*[@id="user_login_email"]')
email.send_keys("teosandu88@gmail.com")
random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)
email = wd.find_element(By.ID, 'user_login_continue')
email.click()

random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)
password = wd.find_element(By.ID, 'user_login_password')
password.send_keys("gabiMARIANA2")
password = wd.find_element(By.ID, 'user_login_continue')    
password.click()
random_wait_time = random.randrange(1, 2)
print(random_wait_time)
time.sleep(random_wait_time)

numerar = wd.find_element(By.XPATH, '//*[@id="paymentSection"]/div[4]/ul/li[3]')
numerar.click()

#last_step = wd.find_element(By.XPATH, '//*[@id="cartCheckoutPage"]/div[1]/div[6]/div/div[3]/button')
#last_step.click()

time.sleep(20)

