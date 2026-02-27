from selenium.webdriver.common.by import By

class RegistrationLocators:    
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    LOGIN_PAGE_HEADER = (By.XPATH, "//h2[text()='Вход']")
    REGISTER_PAGE_HEADER = (By.XPATH, "//h2[text()='Регистрация']")
    
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")
