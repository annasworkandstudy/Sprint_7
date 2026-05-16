import pytest
from api_methods.scooter_methods import ScooterMethods 
from generators import GenerateData


@pytest.fixture
def clean_up_courier():
    courier_data = []
    yield courier_data
    if courier_data:
        body = courier_data[0]
        login_body = {"login": body["login"], "password": body["password"]}
        login_response = ScooterMethods.login_courier(login_body)
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            ScooterMethods.delete_courier(courier_id)

@pytest.fixture
def create_precondition_courier(clean_up_courier):
    body = GenerateData.generate_courier_login_password()
    ScooterMethods.create_courier(body)
    clean_up_courier.append(body)
    return body

@pytest.fixture
def register_and_clean_courier():
    account_data = GenerateData.generate_courier_login_password()
    create_response = ScooterMethods.create_courier(account_data)
    assert create_response.status_code == 201, "Не удалось создать курьера в фикстуре"

    yield account_data

    login_body = {
        "login": account_data["login"],
         "password": account_data["password"]
    }
    login_response = ScooterMethods.login_courier(login_body)
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        ScooterMethods.delete_courier(courier_id)
