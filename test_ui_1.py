from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_search(driver):    
    driver.get("https://www.chitai-gorod.ru/")

    search_input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'header-search-input'))
    search_input_field.send_keys("колобок", Keys.RETURN)
    result = driver.find_element(By.CSS_SELECTOR, "article")
    assert result is not None

def test_clear(driver):    
    driver.get("https://www.chitai-gorod.ru/")

    search_input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CLASS_NAME, 'header-search-input'))
    search_input_field.send_keys("python", Keys.RETURN)
    search_input_field.clear()
    search_input_field.send_keys("SQL", Keys.RETURN)
    result = driver.find_element(By.CSS_SELECTOR, "article")
    assert result is "contains SQL"    

def test_window_size(driver):
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru/")
    driver.set_window_size('window_size',640, 460)
    driver = WebDriverWait(20)
    assert 'window_size' == 640, 460

def test_main_page(driver):
    driver.get("https://www.chitai-gorod.ru/")
    assert "Читай город" in driver.title

def test_add_to_cart(driver):
        driver.get("https://www.chitai-gorod.ru/")
        add_to_cart_button = driver.find_element_by_xpath("//button[contains(text), 'Добавить в корзину']")
        add_to_cart_button.click()
        assert "Книга успешно добавлена в корзину" in driver.page_source