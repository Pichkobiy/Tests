from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

"""Тестирование поисковой строки"""
def test_search(driver):    
    driver.get("https://www.chitai-gorod.ru/")

    search_input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'header-search-input')))
    search_input_field.send_keys("колобок", Keys.RETURN)
    result = driver.find_element_by_css_selector("article")
    assert result is not None
"""Тести
-ьзрование очистки поисковой строки"""
def test_clear(driver):    
    driver.get("https://www.chitai-gorod.ru/")

    search_input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'header-search-input')))
    search_input_field.send_keys("python", Keys.RETURN)
    search_input_field.clear()
    search_input_field.send_keys("SQL", Keys.RETURN)
    result = driver.find_element(By.CSS_SELECTOR, "article")
    assert result is "contains SQL"    

"""Тестирование адаптивности сайта"""
def test_window_size(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru/")
    driver.set_window_size(640, 460)
    driver = WebDriverWait(10)
    assert 'window_size' == 640, 460

"""Тестирование заголовка страницы"""
def test_main_page(driver):
    driver.get("https://www.chitai-gorod.ru/")
    title = driver.find_element(By.CLASS_NAME, "header-logo-icon").text
    assert title == "Читай город"

"""Тестирование корзины"""
def test_add_to_cart(driver):
        driver.get("https://www.chitai-gorod.ru/")
        add_to_cart_button = driver.find_element(By.XPATH,"//button[contains(text), 'Добавить в корзину']")
        add_to_cart_button.click()
        assert "Книга успешно добавлена в корзину" in driver.page_source