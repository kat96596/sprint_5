import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import random
import string


# URL для тестирования
BASE_URL = "https://stellarburgers.education-services.ru"
REGISTER_URL = f"{BASE_URL}/register"
LOGIN_URL = f"{BASE_URL}/login"
PROFILE_URL = f"{BASE_URL}/account/profile"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"

# Список доступных доменов для email (при необходимости можно дополнить)
EMAIL_DOMAINS = [
    'yandex.ru', 
    'ya.ru', 
    'gmail.com', 
    'mail.ru', 
    'yahoo.com', 
    'outlook.com'
]


def generate_random_email():
    first_names = ['john', 'jane', 'alex', 'maria', 'david', 'anna', 'michael', 'elena', 'robert', 'sarah']
    last_names = ['smith', 'johnson', 'williams', 'brown', 'jones', 'garcia', 'miller', 'davis', 'wilson', 'moore']
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    cohort_number = 41
    random_digits = ''.join(random.choices(string.digits, k=3))
    
    domain = random.choice(EMAIL_DOMAINS)
    
    email = f"{first_name}_{last_name}_{cohort_number}_{random_digits}@{domain}"
    
    return email.lower()


def generate_random_password(min_length=6):
    length = random.randint(min_length, min_length + 3)
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    all_chars = lowercase + uppercase + digits
    
    password = ''.join(random.choices(all_chars, k=length))
    
    return password


@pytest.fixture(params=['chrome'])
def driver(request):
    browser = request.param
    
    if browser == 'chrome':
        options = Options()
        options.add_argument('--window-size=1920,1080')
        # Раскомментировать для headless режима
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    email = generate_random_email()
    password = generate_random_password()
    name = "Test User"
    
    driver.get(REGISTER_URL)
    
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[text()='Имя']/following-sibling::input"))
    )
    name_input.send_keys(name)
    
    email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    email_input.send_keys(email)
    
    password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    password_input.send_keys(password)
    
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )
    
    return {
        'email': email,
        'password': password,
        'name': name
    }


# Выбор браузера через командную строку
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