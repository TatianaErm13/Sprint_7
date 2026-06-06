import pytest
import requests

from data import BASE_URL, CREATE_ORDER_PATH


class TestCreateOrder:

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

        response = requests.post(
            f"{BASE_URL}{CREATE_ORDER_PATH}",
            json=payload
        )

        assert response.status_code == 201
        assert "track" in response.json()

        track = response.json()["track"]

        requests.put(
            f"{BASE_URL}/api/v1/orders/cancel",
            params={"track": track}
        )