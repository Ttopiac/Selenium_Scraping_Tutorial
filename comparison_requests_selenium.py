from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import numpy as np
import requests
#Set the PATH varialbe here if you did not set it in your system
# PATH = "D:\Codes\wdi\chromedriver.exe"
# driver = webdriver.Chrome(PATH)

times = 10
selenium_time_cost = 0
for i in np.arange(times):
	driver = webdriver.Chrome()
	wait = WebDriverWait(driver, 10)
	selenium_start = time.time()
	driver.get("https://www.google.com")
	selenium_end = time.time()
	selenium_time_cost += (selenium_end-selenium_start)
	driver.close()

requests_time_cost = 0
for i in np.arange(times):               
	requests_start = time.time()
	r = requests.get("https://www.google.com")
	requests_end = time.time()
	requests_time_cost += requests_end-requests_start

print("Selenium time cost to visit the website: ", selenium_time_cost/times)
print("Requests time cost to visit the website: ", requests_time_cost/times)
