from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# URL для тестирования
BASE_URL = "https://stellarburgers.education-services.ru"
LOGIN_URL = f"{BASE_URL}/login"
PROFILE_URL = f"{BASE_URL}/account/profile"


class TestProfile:
    
    def test_navigate_to_profile(self, driver, registered_user):
        driver.get(LOGIN_URL)
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(PROFILE_URL)
        )
        
        assert driver.current_url == PROFILE_URL
        
        profile_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Профиль']"))
        )
        assert profile_element.is_displayed()
    
    def test_navigate_from_profile_to_constructor_by_click(self, driver, registered_user):
        driver.get(LOGIN_URL)
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(PROFILE_URL)
        )
        
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
        )
        constructor_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        assert driver.current_url in [BASE_URL, BASE_URL + "/"]
        
        constructor_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
        )
        assert constructor_header.is_displayed()
    
    def test_navigate_from_profile_to_constructor_by_logo(self, driver, registered_user):
        driver.get(LOGIN_URL)
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(PROFILE_URL)
        )
        
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a"))
        )
        logo.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        assert driver.current_url in [BASE_URL, BASE_URL + "/"]
        
        constructor_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
        )
        assert constructor_header.is_displayed()
    
    def test_logout_from_profile(self, driver, registered_user):
        driver.get(LOGIN_URL)
        
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input"))
        )
        email_input.send_keys(registered_user['email'])
        
        password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")
        password_input.send_keys(registered_user['password'])
        
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        login_button.click()
        
        WebDriverWait(driver, 10).until(
            lambda x: x.current_url in [BASE_URL, BASE_URL + "/"]
        )
        
        profile_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        )
        profile_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(PROFILE_URL)
        )
        
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
        )
        logout_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(LOGIN_URL)
        )
        
        assert driver.current_url == LOGIN_URL
        
        login_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))
        )
        assert login_header.is_displayed()