class Urls:
    BASE = "https://stellarburgers.education-services.ru"

    API_REGISTER = f"{BASE}/api/auth/register"
    API_LOGIN = f"{BASE}/api/auth/login"
    API_USER = f"{BASE}/api/auth/user"
    API_ORDERS = f"{BASE}/api/orders"
    API_INGREDIENTS = f"{BASE}/api/ingredients"  

class ErrorMessages:
    USER_EXISTS = "User already exists"
    AUTH_REQUIRED = "You should be authorised"
    INGREDIENTS_REQUIRED = "Ingredient ids must be provided"
    WRONG_CREDENTIALS = "email or password are incorrect"
    REQUIRED_FIELDS = "Email, password and name are required fields"


class TestCredentials:
    EMAIL = "test@example.com"
    PASSWORD = "password123"
    NAME = "Test User"
