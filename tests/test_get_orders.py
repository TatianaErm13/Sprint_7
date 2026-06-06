import allure
import requests

from data import (
    BASE_URL,
    GET_ORDERS_PATH
)


class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_returns_orders_list(self):

        response = requests.get(
            f"{BASE_URL}{GET_ORDERS_PATH}"
        )

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
        