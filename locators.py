from selenium.webdriver.common.by import By


class MainPageLocators:
    # Главная страница
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc')]")


class LoginPageLocators:
    # Страница входа
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")


class RegisterPageLocators:
    # Страница регистрации
    REGISTER_HEADER = (By.XPATH, "//h2[text()='Регистрация']")
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")


class ForgotPasswordPageLocators:
    # Восстановление пароля
    FORGOT_PASSWORD_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ProfilePageLocators:
    # Cтраница личного кабинета
    PROFILE_HEADER = (By.XPATH, "//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    PROFILE_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")