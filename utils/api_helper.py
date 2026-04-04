import requests
import time
import string
import random
from data import Urls
import json
import allure

def get_ingredients():
    response = requests.get(Urls.API_INGREDIENTS)
    ingredients_json = response.json()
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients_json["data"]]
    return ingredient_ids


def generate_random_ingredient(length=10):
    letters = string.ascii_lowercase
    random_ingredient = ''.join(random.choice(letters) for i in range(length))
    return random_ingredient


def get_list_invalid_ingredients():
    try:
        ingredients = get_ingredients()
        return [ingredients[0] if ingredients else "invalid_id", generate_random_ingredient()]
    except:
        return ["invalid_id1", generate_random_ingredient()]


def get_random_data_user():
    timestamp = int(time.time())
    random_suffix = random.randint(1000, 9999)

    email = f"test.user.{timestamp}.{random_suffix}@example.com"
    password = f"Pass{timestamp}{random_suffix}!"
    name = f"User{timestamp}{random_suffix}"

    return email, password, name


def generate_random_password(length=8):
    letters = string.ascii_letters
    digits = string.digits
    special = "!@#$%"

    all_chars = letters + digits + special
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password


def generate_random_email():
    timestamp = int(time.time())
    random_suffix = random.randint(1000, 9999)
    return f"user{timestamp}{random_suffix}@example.com"


def generate_random_name(length=6):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(length))
    return random_name.capitalize()

def show_response(response, request_data=None, headers=None):   
    if headers:
        allure.attach(
            json.dumps(headers, indent=2, ensure_ascii=False),
            "Request Headers",
            allure.attachment_type.JSON
        )

    if request_data:
        allure.attach(
            json.dumps(request_data, indent=2, ensure_ascii=False),
            "Request Body",
            allure.attachment_type.JSON
        )

    allure.attach(
        str(response.status_code),
        "Response Status Code",
        allure.attachment_type.TEXT
    )

    try:
        response_json = response.json()
        allure.attach(
            json.dumps(response_json, indent=2, ensure_ascii=False),
            "Response Body",
            allure.attachment_type.JSON
        )
    except:
        allure.attach(
            response.text,
            "Response Body",
            allure.attachment_type.TEXT
    )
