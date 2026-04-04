import requests
import allure
from data import Urls, ErrorMessages
from utils.api_helper import generate_random_email, generate_random_password


class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_existing_user(self, generate_user_data):
        user_data = generate_user_data
        
        with allure.step("Создание пользователя для теста"):
            create_response = requests.post(Urls.API_REGISTER, json=user_data)
            assert create_response.status_code == 200
            token = create_response.json()["accessToken"]
        
        with allure.step("Отправка запроса на логин"):
            login_data = {
                "email": user_data["email"],
                "password": user_data["password"]
            }
            allure.attach(str(login_data), "Login data", allure.attachment_type.JSON)
            login_response = requests.post(Urls.API_LOGIN, json=login_data)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(login_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(login_response.text, "Response body", allure.attachment_type.JSON)
            assert login_response.status_code == 200
        
            login_response_json = login_response.json()
            assert login_response.json()["success"] is True
            assert login_response_json["user"]["email"] == user_data["email"]
            assert login_response_json["user"]["name"] == user_data["name"]
        
        with allure.step("Очистка - удаление пользователя"):
            headers = {"Authorization": token}
            delete_response = requests.delete(Urls.API_USER, headers=headers)
            assert delete_response.status_code == 202

    @allure.title("Логин с неверным паролем")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_password(self, generate_user_data):
        user_data = generate_user_data
        
        with allure.step("Создание пользователя для теста"):
            create_response = requests.post(Urls.API_REGISTER, json=user_data)
            assert create_response.status_code == 200
            token = create_response.json()["accessToken"]
        
        with allure.step("Отправка запроса с неверным паролем"):
            login_data = {
                "email": user_data["email"],
                "password": generate_random_password()
            }
            allure.attach(str(login_data), "Login data", allure.attachment_type.JSON)
            login_response = requests.post(Urls.API_LOGIN, json=login_data)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(login_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(login_response.text, "Response body", allure.attachment_type.JSON)
            assert login_response.status_code == 401
            assert login_response.json()["success"] is False
            assert login_response.json()["message"] == ErrorMessages.WRONG_CREDENTIALS
        
        with allure.step("удаление пользователя"):
            headers = {"Authorization": token}
            delete_response = requests.delete(Urls.API_USER, headers=headers)
            assert delete_response.status_code == 202

    @allure.title("Логин с неверным email")
    @allure.story("Авторизация")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_wrong_email(self, generate_user_data):
        user_data = generate_user_data
        
        with allure.step("Создание пользователя для теста"):
            create_response = requests.post(Urls.API_REGISTER, json=user_data)
            assert create_response.status_code == 200
            token = create_response.json()["accessToken"]
        
        with allure.step("Отправка запроса с неверным email"):
            login_data = {
                "email": generate_random_email(),
                "password": user_data["password"]
            }
            allure.attach(str(login_data), "Login data", allure.attachment_type.JSON)
            login_response = requests.post(Urls.API_LOGIN, json=login_data)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(login_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(login_response.text, "Response body", allure.attachment_type.JSON)
            assert login_response.status_code == 401
            assert login_response.json()["success"] is False
            assert login_response.json()["message"] == ErrorMessages.WRONG_CREDENTIALS
        
        with allure.step("удаление пользователя"):
            headers = {"Authorization": token}
            delete_response = requests.delete(Urls.API_USER, headers=headers)
            assert delete_response.status_code == 202
