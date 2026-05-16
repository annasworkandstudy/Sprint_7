import requests
import allure
from url import URL

class ScooterMethods:

    @staticmethod
    @allure.step('Создаем курьера')
    def create_courier(body):
        return requests.post(url=URL.CREATE_COURIER, json=body)
    
    @staticmethod
    @allure.step('Логирование курьера')
    def login_courier(body):
        return requests.post(url=URL.LOGIN_COURIER, json=body)
    
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(body):
        return requests.post(url=URL.CREATE_ORDER, json=body)
    
    @staticmethod
    @allure.step('Получение списка заказов')
    def get_list_order():
        return requests.get(url=URL.LIST_ORDER)
    
    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_id):
        return requests.delete(url=f"{URL.CREATE_COURIER}/{courier_id}")