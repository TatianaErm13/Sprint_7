import allure

from helpers import generate_courier_data
from courier_methods import create_courier
from data import (
    CREATE_COURIER_ERROR,
    DUPLICATE_LOGIN_ERROR
)


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):

        payload = generate_courier_data()

        response = create_courier(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):

        payload = generate_courier_data()

        create_courier(payload)

        response = create_courier(payload)

        assert response.status_code == 409
        assert response.json()["message"] == DUPLICATE_LOGIN_ERROR

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):

        payload = {
            "password": "12345",
            "firstName": "Ivan"
        }

        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == CREATE_COURIER_ERROR

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):

        payload = {
            "login": "test_login",
            "firstName": "Ivan"
        }

        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()["message"] == CREATE_COURIER_ERROR
        