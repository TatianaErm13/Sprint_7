import pytest

from helpers import generate_courier_data
from courier_methods import (
    create_courier,
    login_courier,
    delete_courier
)


@pytest.fixture
def created_courier():

    payload = generate_courier_data()

    create_courier(payload)

    yield payload

    login_response = login_courier(
        payload["login"],
        payload["password"]
    )

    courier_id = login_response.json()["id"]

    delete_courier(courier_id)
    