from generators import GenerateData
import allure
from api_methods.scooter_methods import ScooterMethods 

class TestLoginCourier():

    @allure.title('Тест на успешное логирование курьера')
    @allure.description('Проверяем, что при корректных данных API возвращает 200 и {"id": id}')
    def test_login_courier(self, register_and_clean_courier):
        account_data = register_and_clean_courier
        login_body = {
            "login": account_data["login"],
            "password": account_data["password"]
        }
        response = ScooterMethods.login_courier(login_body)
        assert response.status_code == 200, f"Ожидался код 200, но получен {response.status_code}. Ответ сервера: {response.text}"
        assert 'id' in response.json()

    @allure.title('Тест на авторизацию несуществующего пользователя')
    @allure.description('Проверяем, что при авторизации несуществующего пользователя API возвращает 404 ')
    def test_login_courier_non_existent(self):
        body = GenerateData.generate_courier_login_password()
        response = ScooterMethods.login_courier(body)
        assert response.status_code == 404, f"Ожидался код 404, но получен {response.status_code}"
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title('Тест на авторизацию без пароля')
    @allure.description('Проверяем, что при авторизации без пароля API возвращает 400 Bad Request')
    def test_login_courier_non_existent_pass(self):
        account_data = GenerateData.generate_courier_login_password()
        login_body = {
            "login": account_data["login"],
            "password": ""
        }
        response = ScooterMethods.login_courier(login_body)
        assert response.status_code == 400, f"Ожидался код 400, но получен {response.status_code}"
        assert response.json().get("message") == "Недостаточно данных для входа"
        