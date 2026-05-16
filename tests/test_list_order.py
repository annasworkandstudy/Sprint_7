import allure
from api_methods.scooter_methods import ScooterMethods

class TestListOrder:

    @allure.title('Тест на успешное полученеи списка заказов')
    @allure.description('Проверяем, что API возвращает 200 и список заказов')
    def test_get_list_order(self):
        response = ScooterMethods.get_list_order()
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}"
