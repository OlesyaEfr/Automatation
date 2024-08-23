from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser.get("https://ya.ru/")

browser.maximize_window()
browser.minimize_window()
browser.fullscreen_window()
browser.set_window_size(1000, 600)

sleep(5)

browser.quit()
