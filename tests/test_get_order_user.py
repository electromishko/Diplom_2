import requests
import allure
from data import Urls, ErrorMessages


class TestGetOrderUser:
    @allure.title("Получение заказов авторизованного пользователя")
    @allure.story("Получение заказов")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_order_authorised_user(self, user_register, create_order_with_ingredients):
        token = user_register["token"]
        headers = {"Authorization": token}
    
        with allure.step("Отправка запроса на получение заказов"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            get_order_response = requests.get(Urls.API_ORDERS, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(get_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(get_order_response.text, "Response body", allure.attachment_type.JSON)
            assert get_order_response.status_code == 200
        
            get_order_response_json = get_order_response.json()
            assert get_order_response_json["success"] is True
            assert "orders" in get_order_response_json

    @allure.title("Получение заказов неавторизованного пользователя")
    @allure.story("Получение заказов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_order_unauthorised_user(self, user_register, create_order_with_ingredients):
        with allure.step("Отправка запроса на получение заказов без авторизации"):
            get_order_response = requests.get(Urls.API_ORDERS)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(get_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(get_order_response.text, "Response body", allure.attachment_type.JSON)
            assert get_order_response.status_code == 401
        
            get_order_response_json = get_order_response.json()
            assert get_order_response_json["success"] is False
            assert get_order_response_json["message"] == ErrorMessages.AUTH_REQUIRED
