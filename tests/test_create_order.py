import pytest
import allure
from generators import GenerateData
from api_methods.scooter_methods import ScooterMethods

class TestCreateOrder:
   
    @allure.title('Тест на успешное создание заказа с разными цветами')
    @allure.description('Проверяем, что API возвращает 201 и номер трека при любых комбинациях цветов')
    @pytest.mark.parametrize("chosen_colors", [
        ["BLACK"],
        ["GREY"],          
        ["BLACK", "GREY"],   
        []                   
    ])
    def test_create_order_success(self, chosen_colors):
        order_body = GenerateData.generate_data_order(color_list=chosen_colors)
        response = ScooterMethods.create_order(order_body)
        assert response.status_code == 201, f"Ожидался код 201, но получен {response.status_code}. Ответ: {response.text}"
        assert "track" in response.json(), f"Ключ 'track' отсутствует в ответе сервера: {response.json()}"
        assert isinstance(response.json()["track"], int), "Номер трека должен быть целым числом"