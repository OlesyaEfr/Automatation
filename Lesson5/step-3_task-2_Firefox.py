from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
driver.get('http://uitestingplayground.com/dynamicid')

driver.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
