import requests

from data import (
    BASE_URL,
    LOGIN_COURIER_PATH,
    LOGIN_ERROR
)


class TestLoginCourier:

    def test_courier_can_login(self, created_courier):

        response = requests.post(
            f"{BASE_URL}{LOGIN_COURIER_PATH}",
            data={
                "login": created_courier[0],
                "password": created_courier[1]
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_without_login(self):

        response = requests.post(
            f"{BASE_URL}{LOGIN_COURIER_PATH}",
            data={
                "password": "12345"
            }
        )

        assert response.status_code == 400
        assert response.json()["message"] == LOGIN_ERROR

    def test_login_without_password(self):

        response = requests.post(
            f"{BASE_URL}{LOGIN_COURIER_PATH}",
            data={
                "login": "test_login",
                "password": ""
            }
        )

        print("\nSTATUS:", response.status_code)
        print("TEXT:", response.text)

        assert response.status_code == 400

    def test_login_with_wrong_password(self, created_courier):

        response = requests.post(
            f"{BASE_URL}{LOGIN_COURIER_PATH}",
            data={
                "login": created_courier[0],
                "password": "wrong_password"
            }
        )

        assert response.status_code == 404

    def test_login_nonexistent_courier(self):

        response = requests.post(
            f"{BASE_URL}{LOGIN_COURIER_PATH}",
            data={
                "login": "nonexistent_login",
                "password": "nonexistent_password"
            }
        )

        assert response.status_code == 404