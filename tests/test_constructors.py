import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.education-services.ru"


class TestConstructor:
    
    def test_navigate_to_buns_section(self, driver):
        driver.get(BASE_URL)
    
        driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").click()
        
        # Небольшая задержка для анимации
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Булки']/parent::div"))
        )
        
        driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").click()
        
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Булки" in active_section.text
    
    def test_navigate_to_sauces_section(self, driver):
        driver.get(BASE_URL)
        
        driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").click()
        
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Соусы" in active_section.text
    
    def test_navigate_to_fillings_section(self, driver):
        driver.get(BASE_URL)
        
        driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").click()
        
        active_section = driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
        assert "Начинки" in active_section.text