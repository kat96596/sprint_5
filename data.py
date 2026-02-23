class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"
    REGISTER_URL = f"{BASE_URL}/register"
    LOGIN_URL = f"{BASE_URL}/login"
    PROFILE_URL = f"{BASE_URL}/account/profile"
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password"


class TestData:
    # Корректные данные для входа
    VALID_EMAIL = "testuser@41143yandex.ru"
    VALID_PASSWORD = "password123"
    
    INVALID_PASSWORD_SHORT = "12345"
    
    BUNS = "Булки"
    SAUCES = "Соусы" 
    FILLINGS = "Начинки"
    
    DEFAULT_TIMEOUT = 10
    SHORT_TIMEOUT = 3