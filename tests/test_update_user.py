import requests
import allure
from data import Urls
from utils.api_helper import get_random_data_user, generate_random_name, generate_random_email, generate_random_password


class TestUpdateUser:
    @allure.title("Изменение всех данных пользователя с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_all_data_with_authorise(self, auth_token):
        token = auth_token
        new_email, new_password, new_name = get_random_data_user()
        new_user_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
        headers = {"Authorization": token}
        update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200

    @allure.title("Изменение поля email с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_email_with_authorise(self, auth_token):
        token = auth_token
        new_email = generate_random_email()
        new_user_data = {"email": new_email}
        headers = {"Authorization": token}
        update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200

    @allure.title("Изменение поля name с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_name_with_authorise(self, auth_token):
        token = auth_token
        new_name = generate_random_name()
        new_user_data = {"name": new_name}
        headers = {"Authorization": token}
        update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)       
        assert update_user_response.status_code == 200

    @allure.title("Изменение поля password с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_password_with_authorise(self, auth_token):
        token = auth_token
        new_password = generate_random_password()
        new_user_data = {"password": new_password}
        headers = {"Authorization": token}
        update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
        assert update_user_response.status_code == 200

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_without_authorise(self, generate_user_data):
        new_email, new_password, new_name = get_random_data_user()
        new_user_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
        update_user_response = requests.patch(Urls.API_USER, json=new_user_data)       
        assert update_user_response.status_code == 401
