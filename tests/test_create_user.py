import pytest
import requests
import allure
from data import Urls, ErrorMessages


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_unique_user(self, user_register):
        user_data = user_register["user_data"]
    
        with allure.step("Проверка созданного пользователя"):
            allure.attach(str(user_data), "User data", allure.attachment_type.JSON)
            response_data = user_register['response_data']
            token = user_register["token"]
        
            assert token is not None
            assert response_data["success"] is True
            assert "user" in response_data
            assert response_data["user"]["email"] == user_data["email"]
            assert response_data["user"]["name"] == user_data["name"]

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_double_user_error(self, user_register):
        user_data = user_register["user_data"]
    
        with allure.step("Попытка создать дубликат пользователя"):
            allure.attach(str(user_data), "Duplicate user data", allure.attachment_type.JSON)
            duplicate_response = requests.post(Urls.API_REGISTER, json=user_data)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(duplicate_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(duplicate_response.text, "Response body", allure.attachment_type.JSON)
            assert duplicate_response.status_code == 403
        
            duplicate_response_json = duplicate_response.json()
            assert duplicate_response_json["success"] is False
            assert duplicate_response_json["message"] == ErrorMessages.USER_EXISTS

    @allure.title("Создание пользователя без обязательных полей")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("user_data,missing_field", [
        ({"email": None, "password": "test123", "name": "Test"}, "email"),
        ({"email": "test@test.com", "password": None, "name": "Test"}, "password"),
        ({"email": "test@test.com", "password": "test123", "name": None}, "name")
    ])
    def test_create_user_without_email_or_password_or_name(self, user_data, missing_field):
        with allure.step(f"Попытка создания пользователя без поля {missing_field}"):
            allure.attach(str(user_data), "User data", allure.attachment_type.JSON)
            response = requests.post(Urls.API_REGISTER, json=user_data)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(response.text, "Response body", allure.attachment_type.JSON)
            assert response.status_code == 403
        
            response_json = response.json()
            assert response_json["success"] is False
            assert response_json["message"] == ErrorMessages.REQUIRED_FIELDS
