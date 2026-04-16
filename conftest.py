import requests
import pytest
from utils.api_helper import get_random_data_user, get_ingredients
from data import Urls


@pytest.fixture
def generate_user_data():
    email, password, name = get_random_data_user()
    user_data = {
        "email": email,
        "password": password,
        "name": name
    }
    return user_data


@pytest.fixture
def auth_token(generate_user_data):
    create_response = requests.post(Urls.API_REGISTER, json=generate_user_data)
    token = create_response.json().get("accessToken") if create_response.status_code == 200 else None
    
    yield token
    
    # Удаление пользователя, если он был создан
    if token:
        headers = {"Authorization": token}
        requests.delete(Urls.API_USER, headers=headers)


@pytest.fixture
def created_user(generate_user_data):
    create_response = requests.post(Urls.API_REGISTER, json=generate_user_data)
    
    result = {
        "user_data": generate_user_data,
        "response_data": None,
        "token": None
    }
    
    if create_response.status_code == 200:
        response_data = create_response.json()
        result["response_data"] = response_data
        result["token"] = response_data.get("accessToken")
    
    yield result
    # Удаление пользователя, если он был создан
    if result["token"]:
        headers = {"Authorization": result["token"]}
        requests.delete(Urls.API_USER, headers=headers)


@pytest.fixture
def ingredients_list():
    return get_ingredients()
