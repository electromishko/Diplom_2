import requests
import pytest
import time
from utils.api_helper import get_random_data_user, get_ingredients
from data import Urls


@pytest.fixture
def user_register():
    email, password, name = get_random_data_user()
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }

    # создание пользователя
    create_response = requests.post(Urls.API_REGISTER, json=user_data)
    assert create_response.status_code == 200, f"Пользователь не был создан, код ответа: {create_response.status_code}, текст: {create_response.text}"

    response_data = create_response.json()

    # получить токен
    token = create_response.json()["accessToken"]
    assert token, f"Токен не был получен: {create_response.text}"

    # данные для авторизации
    yield {
        "user_data": user_data,
        "response_data": response_data,
        "token": token
    }

    # удаление пользователя
    headers = {"Authorization": token}
    delete_response = requests.delete(Urls.API_USER, headers=headers)
    assert delete_response.status_code == 202, f"Ошибка удаления, статус: {delete_response.status_code}, ответ: {delete_response.text}"


@pytest.fixture
def login_user(user_register):
    user_data = user_register["user_data"]
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(Urls.API_LOGIN, json=login_data)
    assert login_response.status_code == 200
    return login_response.json()


@pytest.fixture
def create_order_with_ingredients(user_register, login_user):
    token = user_register["token"]
    headers = {"Authorization": token}
    ingredients_list = get_ingredients()

    if len(ingredients_list) >= 2:
        ingredients = {"ingredients": ingredients_list[:2]}
    else:
        ingredients = {"ingredients": ingredients_list}

    create_order_response = requests.post(Urls.API_ORDERS, json=ingredients, headers=headers)
    assert create_order_response.status_code == 200
    return create_order_response.json()
