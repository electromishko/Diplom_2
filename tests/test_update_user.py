import requests
import allure
from data import Urls, ErrorMessages
from utils.api_helper import get_random_data_user
from utils.api_helper import generate_random_name, generate_random_email, generate_random_password


class TestUpdateUser:
    @allure.title("Изменение всех данных пользователя с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_all_date_with_authorise(self, user_register):
        token = user_register["token"]
        new_email, new_password, new_name = get_random_data_user()
        new_user_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
        headers = {"Authorization": token}
    
        with allure.step("Отправка запроса на изменение всех данных"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            allure.attach(str(new_user_data), "New user data", allure.attachment_type.JSON)
            update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(update_user_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(update_user_response.text, "Response body", allure.attachment_type.JSON)
            assert update_user_response.status_code == 200
        
            update_user_response_json = update_user_response.json()
            assert update_user_response_json["success"] is True
            assert update_user_response_json["user"]["email"] == new_user_data["email"]
            assert update_user_response_json["user"]["name"] == new_user_data["name"]

    @allure.title("Изменение поля email с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_email_with_authorise(self, user_register):
        token = user_register["token"]
        user_data = user_register["user_data"]
        new_email = generate_random_email()
        new_user_data = {"email": new_email}
        headers = {"Authorization": token}
    
        with allure.step("Отправка запроса на изменение email"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            allure.attach(str(new_user_data), "New email", allure.attachment_type.JSON)
            update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(update_user_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(update_user_response.text, "Response body", allure.attachment_type.JSON)
            assert update_user_response.status_code == 200
        
            update_user_response_json = update_user_response.json()
            assert update_user_response_json["success"] is True
            assert update_user_response_json["user"]["email"] == new_email
            assert update_user_response_json["user"]["name"] == user_data["name"]

    @allure.title("Изменение поля name с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_name_with_authorise(self, user_register):
        token = user_register["token"]
        user_data = user_register["user_data"]
        new_name = generate_random_name()
        new_user_data = {"name": new_name}
        headers = {"Authorization": token}
    
        with allure.step("Отправка запроса на изменение name"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            allure.attach(str(new_user_data), "New name", allure.attachment_type.JSON)
            update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(update_user_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(update_user_response.text, "Response body", allure.attachment_type.JSON)
            assert update_user_response.status_code == 200
        
            update_user_response_json = update_user_response.json()
            assert update_user_response_json["success"] is True
            assert update_user_response_json["user"]["email"] == user_data["email"]
            assert update_user_response_json["user"]["name"] == new_name

    @allure.title("Изменение поля password с авторизацией")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user_password_with_authorise(self, user_register):
        token = user_register["token"]
        user_data = user_register["user_data"]
        new_password = generate_random_password()
        new_user_data = {"password": new_password}
        headers = {"Authorization": token}
    
        with allure.step("изменение пароля"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            allure.attach(str(new_user_data), "New password", allure.attachment_type.JSON)
            update_user_response = requests.patch(Urls.API_USER, json=new_user_data, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(update_user_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(update_user_response.text, "Response body", allure.attachment_type.JSON)
            assert update_user_response.status_code == 200
        
            update_user_response_json = update_user_response.json()
            assert update_user_response_json["success"] is True
            assert update_user_response_json["user"]["email"] == user_data["email"]
            assert update_user_response_json["user"]["name"] == user_data["name"]

    @allure.title("Изменение данных пользователя без авторизации")
    @allure.story("Изменение данных пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_update_user_without_authorise(self, user_register):
        new_email, new_password, new_name = get_random_data_user()
        new_user_data = {
            "email": new_email,
            "password": new_password,
            "name": new_name
        }
    
        with allure.step("Отправка запроса на изменение данных без авторизации"):
            allure.attach(str(new_user_data), "New user data", allure.attachment_type.JSON)
            update_user_response = requests.patch(Urls.API_USER, json=new_user_data)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(update_user_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(update_user_response.text, "Response body", allure.attachment_type.JSON)
            assert update_user_response.status_code == 401
            assert update_user_response.json()["success"] is False
            assert update_user_response.json()["message"] == ErrorMessages.AUTH_REQUIRED
