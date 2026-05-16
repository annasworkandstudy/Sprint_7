import time
from faker import Faker

faker = Faker()
class GenerateData:
    @staticmethod
    def generate_courier_login_password():

        unique_suffix = int(time.time() * 1000)
        unique_login = f"{faker.user_name()}_{unique_suffix}"

        return {
            "login": unique_login,
            "password": faker.password(),
            "firstName": faker.first_name()
        }

    @staticmethod
    def generate_data_order(color_list=None):

        if color_list is None:
            color_list = []
        return{     
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.address(),
        "metroStation": f"{faker.city()} - {faker.year()}",
        "phone": faker.phone_number(),
        "rentTime": faker.random_int(min=1, max=30),
        "deliveryDate": faker.date_between(start_date='today', end_date='+30d').isoformat(),
        "comment": faker.sentence(),
        "color": color_list
    }
    