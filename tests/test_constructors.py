import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import Urls
from locators import ConstructorLocators


class TestConstructor:
    
    @pytest.mark.parametrize("section_name, section_locator, expected_text", [
        ("Булки", ConstructorLocators.BUNS_SECTION, "Булки"),
        ("Соусы", ConstructorLocators.SAUCES_SECTION, "Соусы"),
        ("Начинки", ConstructorLocators.FILLINGS_SECTION, "Начинки")
    ])
    def test_navigate_to_section(self, driver, section_name, section_locator, expected_text):
        driver.get(Urls.BASE_URL)
        
        if section_name == "Булки":
            driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
            
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable(ConstructorLocators.BUNS_SECTION)
            )
        
        driver.find_element(*section_locator).click()        
        # Получение активного раздела
        active_section = driver.find_element(*ConstructorLocators.ACTIVE_SECTION)
        
        # Проверка, что активный раздел содержит ожидаемый текст
        assert expected_text in active_section.text
