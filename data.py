class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    REGISTER_URL = f"{BASE_URL}/register"
    LOGIN_URL = f"{BASE_URL}/login"
    PROFILE_URL = f"{BASE_URL}/account/profile"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"


class TestData:
    DEFAULT_USER_NAME = "Test User"
    
    # Некорректные пароли для тестирования
    INVALID_PASSWORDS = [
        "12345",
        "abcde",
        "Abc1",
        "123",
        "qwert",
        "!@#$%"
    ]
    PASSWORD_ERROR_MESSAGE = "Некорректный пароль"
    
    LOGIN_PAGE_HEADER = "Вход"
    REGISTER_PAGE_HEADER = "Регистрация"
    
    BUNS = "Булки"
    SAUCES = "Соусы"
    FILLINGS = "Начинки"
    
    DEFAULT_TIMEOUT = 10
    SHORT_TIMEOUT = 3
