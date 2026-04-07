import requests
import allure
from data import Urls


class TestCreateUser:
    @allure.title("Удаление зарегистрированного пользователя")
    @allure.story("Управление пользователями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_authorized_user(self, generate_user_data):
        create_response = requests.post(Urls.API_REGISTER, json=generate_user_data)
        token = create_response.json().get("accessToken")
        headers = {"Authorization": token}
        delete_response = requests.delete(Urls.API_USER, headers=headers)
        assert delete_response.status_code == 202
