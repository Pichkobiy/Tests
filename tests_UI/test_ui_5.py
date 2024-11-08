from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.chitai-gorod.ru/")
driver.set_window_size(640, 460)
driver = WebDriverWait(10)

driver.quit()


