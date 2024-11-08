from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from config import url

driver = webdriver.Chrome()
driver.get("https://www.chitai-gorod.ru/")

search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'header-search'))
search_button.click()


driver = webdriver.Firefox()
driver.get("https://www.chitai-gorod.ru/")

search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'header-search'))
search_button.click()


driver = webdriver.Edge()
driver.get("https://www.chitai-gorod.ru/")

search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'header-search'))
search_button.click()

driver = webdriver.Chrome()

driver.get("https://www.chitai-gorod.ru/")
search_button = driver.find_element(By.CLASS_NAME, "search-button")

search_button.send_keys("Квесты")
search_button = WebDriverWait(15)
search_button.click()

driver = webdriver.Chrome()
driver.get("https://www.chitai-gorod.ru/")
driver.set_window_size(640, 460)
driver = WebDriverWait(20)

driver.quit()