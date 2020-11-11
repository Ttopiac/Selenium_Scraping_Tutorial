import requests
import numpy as np
import time

times = 3
requests_time_cost = 0
for i in np.arange(times):               
	requests_start = time.time()
	r = requests.get("https://www.google.com")
	requests_end = time.time()
	requests_time_cost += requests_end-requests_start
print(r.text)
print("Requests time cost to visit the website: ", requests_time_cost/times)