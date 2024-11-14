from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys
import allure
from config import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

"""Тестирование поисковой строки"""
def test_search(driver):    
    driver.get(baseURL)

    search_input_field = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'header-search-input')))
    search_input_field.send_keys("колобок", Keys.RETURN)
    result = driver.find_element(By.CSS_SELECTOR, "article")
    assert result is not None
"""Тести
-ьзрование очистки поисковой строки"""
def test_clear(driver):    
    driver.get(baseURL)

    search_input_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'header-search-input')))
    search_input_field.send_keys("python", Keys.RETURN)
    search_input_field.clear()
    search_input_field.send_keys("SQL", Keys.RETURN)
    result = driver.find_element(By.CSS_SELECTOR, "article")
    assert "SQL" in result.text   

"""Тестирование адаптивности сайта"""
def test_window_size(driver):
    driver = webdriver.Chrome()
    driver.get(baseURL)
    driver.set_window_size(640, 460)
    driver = WebDriverWait(30)

    window_size = driver.get_window_size()
    assert window_size['width'] == 640
    assert window_size['height'] == 460
    

"""Тестирование заголовка страницы"""
def test_main_page(driver):
    driver.get(baseURL)
    title = driver.find_element(By.CLASS_NAME, "header-logo_icon").text
    assert title == "Читай город"

"""Тестирование корзины"""
def test_add_to_cart(driver):
        driver.get(baseURL)
        add_to_cart_button = driver.find_element(By.XPATH,"//button[contains(text(), 'Добавить в корзину')]")
        add_to_cart_button.click()
        assert "Книга успешно добавлена в корзину" in driver.page_source