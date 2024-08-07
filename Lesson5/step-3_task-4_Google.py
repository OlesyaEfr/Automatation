from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/entry_ad')
sleep(3)
driver.find_element(By.CSS_SELECTOR, 'div.modal-footer').click()

sleep(3)