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

with open('accountdetails.txt', 'r') as file:
    details = file.readlines()
max_priceint = 0
for i in details[8].strip():   ##strip() for removing the newline character
    max_priceint = max_priceint*10 + int(i)
print(max_priceint)