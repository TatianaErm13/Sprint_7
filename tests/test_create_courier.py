import requests
import random
import string

from data import (
    BASE_URL,
    CREATE_COURIER_PATH,
    CREATE_COURIER_ERROR,
    DUPLICATE_LOGIN_ERROR
)


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


class TestCreateCourier:

    def test_create_courier_success(self):

        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(
            f"{BASE_URL}{CREATE_COURIER_PATH}",
            data=payload
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self):

        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        requests.post(
            f"{BASE_URL}{CREATE_COURIER_PATH}",
            data=payload
        )

        response = requests.post(
            f"{BASE_URL}{CREATE_COURIER_PATH}",
            data=payload
        )

        assert response.status_code == 409
        assert response.json()["message"] == DUPLICATE_LOGIN_ERROR

    def test_create_courier_without_login(self):

        payload = {
            "password": "12345",
            "firstName": "Ivan"
        }

        response = requests.post(
            f"{BASE_URL}{CREATE_COURIER_PATH}",
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == CREATE_COURIER_ERROR

    def test_create_courier_without_password(self):

        payload = {
            "login": generate_random_string(10),
            "firstName": "Ivan"
        }

        response = requests.post(
            f"{BASE_URL}{CREATE_COURIER_PATH}",
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == CREATE_COURIER_ERROR