# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from urls import Urls
from helpers import generate_random_email, generate_random_password


@pytest.fixture(params=['chrome'])
def driver(request):
    browser = request.param
    
    if browser == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)
        
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")
    
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    from locators import RegistrationLocators
    from data import TestData
    
    email = generate_random_email()
    password = generate_random_password()
    name = TestData.DEFAULT_USER_NAME
    
    driver.get(Urls.REGISTER_URL)
    
    name_input = WebDriverWait(driver, TestData.DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located(RegistrationLocators.NAME_INPUT)
    )
    name_input.send_keys(name)
    
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
    
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
    
    WebDriverWait(driver, TestData.DEFAULT_TIMEOUT).until(
        EC.url_to_be(Urls.LOGIN_URL)
    )
    
    return {
        'email': email,
        'password': password,
        'name': name
    }

def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store", 
        default="chrome", 
        help="Browser to run tests: chrome or firefox"
    )

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
