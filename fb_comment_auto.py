from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import credentials
import time

# intializing the driver
driver = webdriver.Chrome()
driver.get('https://web.facebook.com')

# finding email and password box for login
email = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')

# logging in
email.send_keys(credentials.email)
password.send_keys(credentials.password)
password.send_keys(Keys.RETURN)
time.sleep(10)

# heading over to profile
profile = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/a')
profile.click()
time.sleep(20)

# finding the post comment box
commentbox = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div')

# posting comments
for i in range(10):
    commentbox.send_keys('this is an automated comment')
    commentbox.send_keys(Keys.RETURN)
    time.sleep(2)
