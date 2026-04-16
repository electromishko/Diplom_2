import requests
import allure
from data import Urls


class TestGetOrderUser:

    @allure.title("Получение заказов авторизованного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_order_authorised_user(self, auth_token):
        headers = {"Authorization": auth_token}
        with allure.step("Отправка запроса на получение заказов"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            get_order_response = requests.get(Urls.API_ORDERS, headers=headers)
        with allure.step("Проверка ответа"):
            assert get_order_response.status_code == 200

    @allure.title("Получение заказов неавторизованного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_order_unauthorised_user(self):
        with allure.step("Отправка запроса на получение заказов без авторизации"):
            get_order_response = requests.get(Urls.API_ORDERS)
        with allure.step("Проверка ответа"):
            allure.attach(get_order_response.text, "Response body", allure.attachment_type.JSON)
            assert get_order_response.status_code == 401
