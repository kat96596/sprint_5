import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from urls import Urls
from locators import ConstructorLocators


class TestConstructor:

    def test_navigate_to_buns_section(self, driver):
        driver.get(Urls.BASE_URL)
        
        driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
        
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable(ConstructorLocators.BUNS_SECTION)
        )
        
        driver.find_element(*ConstructorLocators.BUNS_SECTION).click()
        
        active_section = driver.find_element(*ConstructorLocators.ACTIVE_SECTION)
        assert "Булки" in active_section.text
    
    def test_navigate_to_sauces_section(self, driver):
        driver.get(Urls.BASE_URL)
        
        driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
        
        active_section = driver.find_element(*ConstructorLocators.ACTIVE_SECTION)
        assert "Соусы" in active_section.text
    
    def test_navigate_to_fillings_section(self, driver):
        driver.get(Urls.BASE_URL)
        
        driver.find_element(*ConstructorLocators.FILLINGS_SECTION).click()
        
        active_section = driver.find_element(*ConstructorLocators.ACTIVE_SECTION)
        assert "Начинки" in active_section.text
