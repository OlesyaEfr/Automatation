from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.set_window_size(640, 460)
for x in range(1, 4):
        driver.back()
        driver.forward()

driver.save_screenshot("./ya.png")

sleep(10)
