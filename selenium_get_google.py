from selenium import webdriver
import numpy as np
import time

times = 3
selenium_time_cost = 0
for i in np.arange(times):
	driver = webdriver.Chrome()
	selenium_start = time.time()
	driver.get("https://www.google.com")
	selenium_end = time.time()
	selenium_time_cost += (selenium_end-selenium_start)
	print(driver)  
	print(i, "")   
	driver.close()
print("Selenium time cost to visit the website: ", selenium_time_cost/times)



