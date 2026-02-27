# test_registration.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from urls import Urls
from data import TestData
from helpers import generate_random_email, generate_random_password
from locators import RegistrationLocators


class TestRegistration:
    
    def test_successful_registration(self, driver):
        email = generate_random_email()
        password = generate_random_password()
        name = TestData.DEFAULT_USER_NAME
        
        driver.get(Urls.REGISTER_URL)
        
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
        
        WebDriverWait(driver, TestData.DEFAULT_TIMEOUT).until(
            EC.url_to_be(Urls.LOGIN_URL)
        )
        
        assert driver.current_url == Urls.LOGIN_URL
        assert driver.find_element(*RegistrationLocators.LOGIN_PAGE_HEADER).is_displayed()
    
    @pytest.mark.parametrize("password", TestData.INVALID_PASSWORDS)
    def test_registration_with_short_password_error(self, driver, password):
        email = generate_random_email()
        name = TestData.DEFAULT_USER_NAME
        
        driver.get(Urls.REGISTER_URL)
        
        driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        
        driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
        
        error_element = WebDriverWait(driver, TestData.DEFAULT_TIMEOUT).until(
            EC.presence_of_element_located(RegistrationLocators.PASSWORD_ERROR)
        )
        assert error_element.is_displayed()
        
        assert driver.current_url == Urls.REGISTER_URL
