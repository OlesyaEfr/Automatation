from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

for i in range(5):
    addElButton = driver.find_element(By.XPATH, ("//button[text()='Add Element']")).click()

numDelButton = driver.find_elements(By.XPATH, ("//button[text()='Delete']"))
print(len(numDelButton))