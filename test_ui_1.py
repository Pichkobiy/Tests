from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from config import url

driver = webdriver.Chrome()
driver.get("https://www.chitai-gorod.ru/")

search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'header-search'))
search_button.click()
driver.quit()