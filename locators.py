from selenium.webdriver.common.by import By


class RegistrationLocators:    
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    LOGIN_PAGE_HEADER = (By.XPATH, "//h2[text()='Вход']")
    REGISTER_PAGE_HEADER = (By.XPATH, "//h2[text()='Регистрация']")
    
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")


class ConstructorLocators:
    
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


class LoginLocators:
    
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class ProfileLocators:
    
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
