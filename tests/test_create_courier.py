from generators import GenerateData
import allure
from api_methods.scooter_methods import ScooterMethods 
from data import Data

class TestCreateCourier:

    @allure.title('Тест на создание курьера')
    @allure.description('Проверяем, что при корректных данных API возвращает 201 и {"ok": true}')
    def test_create_courier_successfull(self, clean_up_courier):
        body = GenerateData.generate_courier_login_password()
        response = ScooterMethods.create_courier(body)
        clean_up_courier.append(body)
        assert response.status_code == 201, f"Ожидался код 201, но получен {response.status_code}"
        assert response.json().get("ok") is True

    @allure.title('Тест на ошибку при создании дубликата курьера')
    @allure.description('Проверяем, что повторный запрос с тем же логином возвращает 409 Conflict')
    def test_create_duplicate_courier_conflict(self, create_precondition_courier):
        body = create_precondition_courier
        duplicate_response = ScooterMethods.create_courier(body)
        assert duplicate_response.status_code == 409, f"Ожидался код 409, но получен {duplicate_response.status_code}"
        assert duplicate_response.json().get("message") == "Этот логин уже используется. Попробуйте другой."
    
    @allure.title('Тест на ошибку при отсутствии одного из полей')
    @allure.description('Проверяем, что при отсутствии одного из полей регистрация невозможна')
    def test_create_courier_without_first_name(self):
        body = Data.data_for_login()
        response = ScooterMethods.create_courier(body)
        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"
        