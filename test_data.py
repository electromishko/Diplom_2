class UserTestData:
    """Тестовые данные для пользователей"""
    
    # Наборы данных для тестирования создания пользователя без обязательных полей
    INVALID_USER_DATA = [
        ({"email": None, "password": "test123", "name": "Test"}, "email"),
        ({"email": "test@test.com", "password": None, "name": "Test"}, "password"),
        ({"email": "test@test.com", "password": "test123", "name": None}, "name")
    ]
