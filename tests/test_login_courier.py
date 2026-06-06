import allure

from courier_methods import login_courier
from data import LOGIN_ERROR


class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_courier_can_login(self, created_courier):

        response = login_courier(
            created_courier["login"],
            created_courier["password"]
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация без логина")
    def test_login_without_login(self):

        response = login_courier(
            "",
            "12345"
        )

        assert response.status_code == 400
        assert response.json()["message"] == LOGIN_ERROR

    @allure.title("Авторизация без пароля")
    def test_login_without_password(self):

        response = login_courier(
            "test_login",
            ""
        )

        assert response.status_code == 400

    @allure.title("Авторизация с неверным паролем")
    def test_login_with_wrong_password(self, created_courier):

        response = login_courier(
            created_courier["login"],
            "wrong_password"
        )

        assert response.status_code == 404

    @allure.title("Авторизация несуществующего курьера")
    def test_login_nonexistent_courier(self):

        response = login_courier(
            "nonexistent_login",
            "nonexistent_password"
        )

        assert response.status_code == 404
        