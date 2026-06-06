import pytest
import requests

from helpers import register_new_courier_and_return_login_password
from data import (
    BASE_URL,
    LOGIN_COURIER_PATH,
    DELETE_COURIER_PATH
)


@pytest.fixture
def created_courier():

    courier = register_new_courier_and_return_login_password()

    login = courier[0]
    password = courier[1]

    login_response = requests.post(
        f"{BASE_URL}{LOGIN_COURIER_PATH}",
        data={
            "login": login,
            "password": password
        }
    )

    courier_id = login_response.json()["id"]

    yield courier

    requests.delete(
        f"{BASE_URL}{DELETE_COURIER_PATH}/{courier_id}"
    )