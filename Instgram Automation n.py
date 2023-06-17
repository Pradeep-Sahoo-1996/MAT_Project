#Automate the Instagram Account and OPen the Profile Page...

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
path = "G:\@PYTHON@\Selenium\Selenium pratice\chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")
driver.implicitly_wait(2)
print('The Url is Open')
#Login Page 
#Username text field
_username = driver.find_element_by_css_selector("input[class='_aa4b _add6 _ac4d']")
_username.click()
driver.implicitly_wait(1)
_username.send_keys("Enter_Your_User_Name")
driver.implicitly_wait(1)
#Password text field 
_password = driver.find_element_by_css_selector("input[type='password']")
_password.click()
driver.implicitly_wait(2)
_password.send_keys('Enter_Your_Password')
driver.implicitly_wait(2)
print("The Username and Password is entered")
#Login button
_login = driver.find_element_by_css_selector("div[class = 'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
_login.click()
print('Welcome To Instgram')
driver.implicitly_wait(2)
#Save Info
#Windows pupup Handeling 
handles = driver.window_handles
driver.switch_to.window(handles[0])
driver.implicitly_wait(2)
_save = driver.find_element_by_xpath("//button[@class ='_acan _acap _acas _aj1-']").click()
print("The Login Info Is Save...")
driver.implicitly_wait(3)
_notification_page = driver.find_element_by_css_selector("div[class = '_aake']")
_notification = driver.find_element_by_css_selector("button[class= '_a9-- _a9_1']").click()
print("The Notification Page is Opened... and close")
driver.implicitly_wait(3)
#Profile page 
#Maximize the window 
driver.maximize_window()
driver.implicitly_wait(2)
_profile = driver.find_element_by_xpath('//a[@class = "x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aak1 _a6hd"]')
_profile.click()
driver.implicitly_wait(3)
print('Your Instgram Profile is open')

driver.quit()
driver.implicitly_wait(1)