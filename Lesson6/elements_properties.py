from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://ya.ru/")

txt = driver.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text

print(txt)
driver.quit() 