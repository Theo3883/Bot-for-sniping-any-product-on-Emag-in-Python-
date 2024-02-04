from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
import time

options = webdriver.ChromeOptions()
options.add_extension('./captcha.crx')
driver = webdriver.Chrome(options=options) 
driver.get('http://www.google.com')
time.sleep(10)