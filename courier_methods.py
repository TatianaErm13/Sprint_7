import allure
import requests

from data import (
    BASE_URL,
    CREATE_COURIER_PATH,
    LOGIN_COURIER_PATH,
    DELETE_COURIER_PATH
)


@allure.step("Создать курьера")
def create_courier(payload):
    return requests.post(
        f"{BASE_URL}{CREATE_COURIER_PATH}",
        data=payload
    )


@allure.step("Авторизовать курьера")
def login_courier(login, password):
    return requests.post(
        f"{BASE_URL}{LOGIN_COURIER_PATH}",
        data={
            "login": login,
            "password": password
        }
    )


@allure.step("Удалить курьера")
def delete_courier(courier_id):
    return requests.delete(
        f"{BASE_URL}{DELETE_COURIER_PATH}/{courier_id}"
    )
