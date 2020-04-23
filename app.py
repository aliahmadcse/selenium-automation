from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://wiki.python.org/moin/FrontPage")

# search = driver.find_element_by_id("searchinput")

# search.send_keys("Beginner")
# search.send_keys(Keys.RETURN)

select=Select(driver.find_element_by_xpath('//*[@id="sidebar"]/div[3]/ul/li[5]/form/div/select'))
select.select_by_index(1)

# driver.close()
