import pytest
import requests
import allure

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Store")
class TestStore:
    @allure.title("Размещение заказа")
    def test_place_an_order(self):
        with allure.step("Подготовка данных для размещение заказа"):
            payload = {
                "id": 1,
                "petId": 1,
                "quantity": 1,
                "status": "placed",
                "complete": True
            }
        with allure.step("Отправка запроса на размещение заказа"):
            response = requests.post(url=f"{BASE_URL}/store/order", json=payload)
            response_json = response.json()

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка данных размещенного заказа"):
            assert response_json["id"] == payload["id"], "id заказа не совпадает с ожидаемым"
            assert response_json["petId"] == payload["petId"], "id питомца не совпадает с ожидаемым"
            assert response_json["quantity"] == payload["quantity"], "количество не совпадает с ожидаемым"
            assert response_json["status"] == payload["status"], "статус заказа не совпадает с ожидаемым"
            assert response_json["complete"] == payload["complete"], "статус завершения заказа не совпадает с ожидаемым"

    @allure.title("Получение информации о заказе по id")
    def test_get_order_info_by_id(self, place_an_order):
        with allure.step("Получение данных размещенного заказа"):
            order_id = place_an_order["id"]
            pet_id = place_an_order["petId"]
            quantity = place_an_order["quantity"]
            status = place_an_order["status"]
            complete = place_an_order["complete"]

        with allure.step("Отправка запроса на получение информации о заказе по id"):
            response = requests.get(url=f"{BASE_URL}/store/order/{order_id}")
            response_json = response.json()

        with allure.step("Проверка статуса ответа и данных заказа"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            assert response_json["id"] == order_id, "id заказа не совпадает с ожидаемым"
            assert response_json["petId"] == pet_id, "id питомца не совпадает с ожидаемым"
            assert response_json["quantity"] == quantity, "количество не совпадает с ожидаемым"
            assert response_json["status"] == status, "статус заказа не совпадает с ожидаемым"
            assert response_json["complete"] == complete, "статус завершения заказа не совпадает с ожидаемым"
