from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/login')

username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('tomsmith')
sleep(2)
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('SuperSecretPassword!')
sleep(2)
login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login_button.click()
sleep(3)