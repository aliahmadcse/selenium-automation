# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time

# driver = webdriver.Chrome()

# driver.get('http://jqueryui.com/droppable')
# driver.switch_to.frame(0)

# action_chain = ActionChains(driver)

# source = driver.find_element_by_id('draggable')
# destination = driver.find_element_by_id('droppable')

# action_chain.drag_and_drop_by_offset(source, 10, 10).perform()
# time.sleep(3)

# action_chain.drag_and_drop(source, destination).perform()
# time.sleep(3)

# driver.close()