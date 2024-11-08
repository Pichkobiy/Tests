from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://www.chitai-gorod.ru/")
search_button = driver.find_element(By.CLASS_NAME, "search-button")

search_button.send_keys("Стивен Кинг")
search_button = WebDriverWait(5)
search_button.click()



driver.quit()