import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# URL для тестирования
BASE_URL = "https://stellarburgers.education-services.ru"
LOGIN_URL = f"{BASE_URL}/login"
REGISTER_URL = f"{BASE_URL}/register"
FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"


class TestLogin:
    
    def test_login_via_main_page_login_button(self, driver, registered_user):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        driver.get(BASE_URL)
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        )
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert profile_button.is_displayed()
    
    def test_login_via_profile_button(self, driver, registered_user):
        """Вход через кнопку 'Личный кабинет'"""
        driver.get(BASE_URL)
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert profile_button.is_displayed()
    
    def test_login_via_registration_form(self, driver, registered_user):
        driver.get(REGISTER_URL)
        
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        )
        login_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        # Проверяем, что кнопка "Личный Кабинет" отображается
        profile_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert profile_button.is_displayed()
    
    def test_login_via_forgot_password_form(self, driver, registered_user):
        """Вход через форму восстановления пароля"""
        driver.get(FORGOT_PASSWORD_URL)
        
        # Ждем появления и кликаем по ссылке "Войти"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        )
        login_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        assert profile_button.is_displayed()