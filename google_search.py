from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


# Set the keyword
if len(sys.argv)<=1:
	keyword = "top stories"
	sleeptime = 5
elif len(sys.argv)<=2:
	keyword = sys.argv[1]
	sleeptime = 5
else: 
	keyword = sys.argv[1]
	sleeptime = int(sys.argv[2])

###############################################################################
# STEP 1: Get to a web page
###############################################################################
#Set the PATH varialbe here if you did not set it in your system
driver = webdriver.Chrome()
driver.get("https://www.google.com")

###############################################################################
# STEP 3: Find the element
###############################################################################
# Find the element for givining a keyword of searching
element = driver.find_element_by_name("q")

###############################################################################
# STEP 4 Interact with the element
###############################################################################
# # Google by the key word "top stories"
element.send_keys(keyword)
time.sleep(sleeptime)
element.send_keys(Keys.ENTER)

###############################################################################
# STEP 2/3/4: Wait / Find the element / Interact with the element
###############################################################################
# Wait Until the news button is showing and then click
time.sleep(sleeptime)
wait = WebDriverWait(driver, 10)
wait.until(
	EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'News')]"))
).click()


###############################################################################
# STEP 2/3/4: Wait / Find the element / Interact with the element
###############################################################################
#Extract the search results on news section
wait.until( EC.presence_of_element_located((By.XPATH, "//div[@id='rso']/div[1]/g-card/div/div/div[2]/a/div/div[2]/div[2]")) )
allSearchResults = driver.find_elements_by_xpath("//div[@id='rso']/*/g-card/div/div/div[2]/a")
for eachresult in allSearchResults:
	print(eachresult.text)
	print(eachresult.get_attribute('href'))
	print("")
print("--------------------------------------------------------------------")
time.sleep(sleeptime)

###############################################################################
# STEP 2/3/4: Wait / Find the element / Interact with the element
###############################################################################
#Wait Until the All button is showing and then click
wait.until(
	EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'All')]"))
).click()
#Extract the search results on news section
wait.until( EC.presence_of_element_located((By.XPATH, "//div[1]/div/a/h3/span")))
allSearchResults = driver.find_elements_by_xpath("//div[@id='rso']/*/*/div/a")
for eachresult in allSearchResults:
	print(eachresult.text)
	print(eachresult.get_attribute('href'))
	print("")
time.sleep(sleeptime)

###############################################################################
# STEP 5 Close the browser
###############################################################################
driver.close()

























# Cheet Sheet
# Selenium provides the following methods to locate elements in a page:
# 	find_element_by_id
# 	find_element_by_name
# 	find_element_by_xpath
# 	find_element_by_link_text
# 	find_element_by_partial_link_text
# 	find_element_by_tag_name
# 	find_element_by_class_name
# 	find_element_by_css_selector
# To find multiple elements (these methods will return a list):
#     find_elements_by_name
#     find_elements_by_xpath
#     find_elements_by_link_text
#     find_elements_by_partial_link_text
#     find_elements_by_tag_name
#     find_elements_by_class_name
#     find_elements_by_css_selector
# class selenium.webdriver.common.by.By[source]
# 	Set of supported locator strategies.
# 	CLASS_NAME = 'class name'
# 	CSS_SELECTOR = 'css selector'
# 	ID = 'id'
# 	LINK_TEXT = 'link text'
# 	NAME = 'name'
# 	PARTIAL_LINK_TEXT = 'partial link text'
# 	TAG_NAME = 'tag name'
# 	XPATH = 'xpath'
# class selenium.webdriver.common.keys.Keys[source]
# 	Set of special keys codes.
# 	ADD = '\ue025'
# 	ALT = '\ue00a'
# 	ARROW_DOWN = '\ue015'
# 	ARROW_LEFT = '\ue012'
# 	ARROW_RIGHT = '\ue014'
# 	ARROW_UP = '\ue013'
# 	BACKSPACE = '\ue003'
# 	BACK_SPACE = '\ue003'
# 	CANCEL = '\ue001'
# 	CLEAR = '\ue005'
# 	COMMAND = '\ue03d'
# 	CONTROL = '\ue009'
# 	DECIMAL = '\ue028'
# 	DELETE = '\ue017'
# 	DIVIDE = '\ue029'
# 	DOWN = '\ue015'
# 	END = '\ue010'
# 	ENTER = '\ue007'
# 	EQUALS = '\ue019'
# 	ESCAPE = '\ue00c'
# 	F1 = '\ue031'
# 	F10 = '\ue03a'
# 	F11 = '\ue03b'
# 	F12 = '\ue03c'
# 	F2 = '\ue032'
# 	F3 = '\ue033'
# 	F4 = '\ue034'
# 	F5 = '\ue035'
# 	F6 = '\ue036'
# 	F7 = '\ue037'
# 	F8 = '\ue038'
# 	F9 = '\ue039'
# 	HELP = '\ue002'
# 	HOME = '\ue011'
# 	INSERT = '\ue016'
# 	LEFT = '\ue012'
# 	LEFT_ALT = '\ue00a'
# 	LEFT_CONTROL = '\ue009'
# 	LEFT_SHIFT = '\ue008'
# 	META = '\ue03d'
# 	MULTIPLY = '\ue024'
# 	NULL = '\ue000'
# 	NUMPAD0 = '\ue01a'
# 	NUMPAD1 = '\ue01b'
# 	NUMPAD2 = '\ue01c'
# 	NUMPAD3 = '\ue01d'
# 	NUMPAD4 = '\ue01e'
# 	NUMPAD5 = '\ue01f'
# 	NUMPAD6 = '\ue020'
# 	NUMPAD7 = '\ue021'
# 	NUMPAD8 = '\ue022'
# 	NUMPAD9 = '\ue023'
# 	PAGE_DOWN = '\ue00f'
# 	PAGE_UP = '\ue00e'
# 	PAUSE = '\ue00b'
# 	RETURN = '\ue006'
# 	RIGHT = '\ue014'
# 	SEMICOLON = '\ue018'
# 	SEPARATOR = '\ue026'
# 	SHIFT = '\ue008'
# 	SPACE = '\ue00d'
# 	SUBTRACT = '\ue027'
# 	TAB = '\ue004'
# 	UP = '\ue013'

# Expected Condition
# 	title_is
# 	title_contains
# 	presence_of_element_located
# 	visibility_of_element_located
# 	visibility_of
# 	presence_of_all_elements_located
# 	text_to_be_present_in_element
# 	text_to_be_present_in_element_value
# 	frame_to_be_available_and_switch_to_it
# 	invisibility_of_element_located
# 	element_to_be_clickable
# 	staleness_of
# 	element_to_be_selected
# 	element_located_to_be_selected
# 	element_selection_state_to_be
# 	element_located_selection_state_to_be
# 	alert_is_present

# selenium.webdriver.remote.webelement
# 	clear()[source]
# 	    Clears the text if it’s a text entry element.
# 	click()[source]
# 	    Clicks the element.
# 	send_keys(*value)
# 		Simulates typing into the element.
# 	screenshot(filename)
# 		Saves a screenshot of the current element to a PNG image file
# 	get_attribute(name)
# 		Gets the given attribute or property of the element.
# 	text
# 	    The text of the element.