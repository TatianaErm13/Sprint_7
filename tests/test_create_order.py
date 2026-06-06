import allure
import pytest

from order_methods import (
    create_order,
    cancel_order
)


class TestCreateOrder:

    @allure.title("Создание заказа с различными вариантами цвета")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    def test_create_order(self, color):

        payload = {
            "firstName": "Naruto",
            "lastName": "Uzumaki",
            "address": "Konoha",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 5,
            "deliveryDate": "2026-06-10",
            "comment": "Saske",
            "color": color
        }

        response = create_order(payload)

        assert response.status_code == 201
        assert "track" in response.json()

        track = response.json()["track"]

        cancel_order(track)
        