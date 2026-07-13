import allure
import requests

from data import (
    BASE_URL,
    CREATE_ORDER_PATH,
    CANCEL_ORDER_PATH
)


@allure.step("Создать заказ")
def create_order(payload):
    return requests.post(
        f"{BASE_URL}{CREATE_ORDER_PATH}",
        json=payload
    )


@allure.step("Отменить заказ")
def cancel_order(track):
    return requests.put(
        f"{BASE_URL}{CANCEL_ORDER_PATH}",
        params={"track": track}
    )
