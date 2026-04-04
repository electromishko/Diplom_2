import requests
import allure
from data import Urls, ErrorMessages
from utils.api_helper import get_ingredients, get_list_invalid_ingredients


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.story("Создание заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_ingredients_with_authorise(self, auth_token, ingredients_list):

        token = auth_token
        headers = {"Authorization": token}
        ingredients = {"ingredients": ingredients_list[:2]}
    
        with allure.step("Отправка запроса на создание заказа"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            allure.attach(str(ingredients), "Request body", allure.attachment_type.JSON)
            create_order_response = requests.post(Urls.API_ORDERS, json=ingredients, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(create_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(create_order_response.text, "Response body", allure.attachment_type.JSON)
            assert create_order_response.status_code == 200
        
            create_order_response_json = create_order_response.json()
            assert create_order_response_json["success"] is True
            assert create_order_response_json["name"] == "Флюоресцентный бессмертный бургер"
            assert len(create_order_response_json["order"]["ingredients"]) == 2
            assert create_order_response_json["order"]["status"] == 'done'

    @allure.title("Создание заказа с авторизацией без ингредиентов")
    @allure.story("Создание заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_without_ingredients_with_authorise(self, auth_token):
        token = auth_token
        headers = {"Authorization": token}
    
        with allure.step("Отправка запроса на создание заказа без ингредиентов"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            create_order_response = requests.post(Urls.API_ORDERS, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(create_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(create_order_response.text, "Response body", allure.attachment_type.JSON)
            assert create_order_response.status_code == 400
        
            create_order_response_json = create_order_response.json()
            assert create_order_response_json["success"] is False
            assert create_order_response_json["message"] == ErrorMessages.INGREDIENTS_REQUIRED

    @allure.title("Создание заказа без авторизации с ингредиентами")
    @allure.story("Создание заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_with_ingredients_without_authorise(self, ingredients_list):
        ingredients = {"ingredients": ingredients_list[:2]}
    
        with allure.step("Отправка запроса на создание заказа без авторизации"):
            allure.attach(str(ingredients), "Request body", allure.attachment_type.JSON)
            create_order_response = requests.post(Urls.API_ORDERS, json=ingredients)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(create_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(create_order_response.text, "Response body", allure.attachment_type.JSON)
            assert create_order_response.status_code == 200
        
            create_order_response_json = create_order_response.json()
            assert create_order_response_json["success"] is True
            assert create_order_response_json["name"] == "Флюоресцентный бессмертный бургер"
            assert "order" in create_order_response_json
            assert create_order_response_json["order"]["number"] is not None

    @allure.title("Создание заказа без авторизации без ингредиентов")
    @allure.story("Создание заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_without_ingredients_without_authorise(self):
        with allure.step("Отправка запроса на создание заказа без авторизации и ингредиентов"):
            create_order_response = requests.post(Urls.API_ORDERS)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(create_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(create_order_response.text, "Response body", allure.attachment_type.JSON)
            assert create_order_response.status_code == 400
        
            create_order_response_json = create_order_response.json()
            assert create_order_response_json["success"] is False
            assert create_order_response_json["message"] == ErrorMessages.INGREDIENTS_REQUIRED

    @allure.title("Создание заказа c неверным хешем ингредиентов")
    @allure.story("Создание заказа")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_with_wrong_id_ingredient(self, auth_token):
        token = auth_token
        headers = {"Authorization": token}
        ingredients = {"ingredients": get_list_invalid_ingredients()}
    
        with allure.step("Отправка запроса с неверными ингредиентами"):
            allure.attach(str(headers), "Headers", allure.attachment_type.TEXT)
            allure.attach(str(ingredients), "Request body", allure.attachment_type.JSON)
            create_order_response = requests.post(Urls.API_ORDERS, json=ingredients, headers=headers)
    
        with allure.step("Проверка ответа"):
            allure.attach(str(create_order_response.status_code), "Status code", allure.attachment_type.TEXT)
            allure.attach(create_order_response.text, "Response body", allure.attachment_type.JSON)
            assert create_order_response.status_code == 500
