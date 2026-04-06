import requests
import allure
from data import Urls, ErrorMessages
from utils.api_helper import generate_random_email, generate_random_password


class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_existing_user(self, created_user):
        user_data = created_user["user_data"]       
        login_data = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        login_response = requests.post(Urls.API_LOGIN, json=login_data)
        assert login_response.status_code == 200

    @allure.title("Логин с неверным паролем")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_password(self, created_user):
        user_data = created_user["user_data"]
        login_data = {
            "email": user_data["email"],
            "password": generate_random_password()
        }
        login_response = requests.post(Urls.API_LOGIN, json=login_data)
        assert login_response.status_code == 401

    @allure.title("Логин с неверным email")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_email(self, created_user):
        user_data = created_user["user_data"]
        
        login_data = {
            "email": generate_random_email(),
            "password": user_data["password"]
        }
        login_response = requests.post(Urls.API_LOGIN, json=login_data)
        assert login_response.status_code == 401
