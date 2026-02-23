import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string

# URL для тестирования
REGISTER_URL = "https://stellarburgers.education-services.ru/register"
LOGIN_URL = "https://stellarburgers.education-services.ru/login"


def generate_random_email():
    first_names = ['john', 'jane', 'alex', 'maria', 'david', 'anna']
    last_names = ['smith', 'johnson', 'williams', 'brown', 'jones']
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{first_name}_{last_name}_6_{random_digits}@yandex.ru"


def generate_short_password():
    length = random.randint(3, 5)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class TestRegistration:
    
    def test_successful_registration(self, driver):
        # Переход на страницу регистрации
        driver.get(REGISTER_URL)
        email = generate_random_email()
        password = generate_random_password()  
        name = "Test User"
        
        # Заполнение формы регистрации
        driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
        
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 5).until(
            EC.url_to_be(LOGIN_URL)
        )
        
        # Проверка, что мы на странице входа
        assert driver.current_url == LOGIN_URL
        assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed()
    
    @pytest.mark.parametrize("password", [
        "12345",
        "abcde",
        "Abc1"
    ])
    def test_registration_with_short_password_error(self, driver, password):
        driver.get(REGISTER_URL)
        email = generate_random_email()
        name = "Test User"
        driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").send_keys(password)
        
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        # Проверка появления ошибки
        error_element = driver.find_element(By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")
        assert error_element.is_displayed()
        
        # Проверка, что мы остались на странице регистрации
        assert driver.current_url == REGISTER_URL


# Вспомогательная функция для генерации пароля (из conftest)
def generate_random_password(min_length=6):
    length = random.randint(min_length, min_length + 3)
    all_chars = string.ascii_letters + string.digits
    return ''.join(random.choices(all_chars, k=length))