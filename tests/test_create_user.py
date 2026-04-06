import pytest
import requests
import allure
from data import Urls
from test_data import UserTestData


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_unique_user(self, generate_user_data):
        user_data = generate_user_data
        create_response = requests.post(Urls.API_REGISTER, json=user_data)       
        assert create_response.status_code == 200

    @allure.title("Создание пользователя, который уже зарегистрирован")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_double_user_error(self, generate_user_data):
        user_data = generate_user_data
        first_response = requests.post(Urls.API_REGISTER, json=user_data)
        token = first_response.json()["accessToken"]
        duplicate_response = requests.post(Urls.API_REGISTER, json=user_data)
        headers = {"Authorization": token}
        requests.delete(Urls.API_USER, headers=headers)
        assert duplicate_response.status_code == 403

    @allure.title("Создание пользователя без обязательных полей")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("user_data,missing_field", UserTestData.INVALID_USER_DATA)
    def test_create_user_without_email_or_password_or_name(self, user_data, missing_field):
        response = requests.post(Urls.API_REGISTER, json=user_data)
        assert response.status_code == 403
