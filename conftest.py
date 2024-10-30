import pytest
from helper import Helper
from methods.courier_methods import CourierMethods


@pytest.fixture(scope='class')
def courier():
    random_credentials = Helper.generate_random_correct_credentials()
    response = CourierMethods.courier_create(random_credentials)
    assert response.status_code == 201 and response.json() == {'ok': True}, 'Не удалось создать курьера'
    yield random_credentials
    response = CourierMethods.courier_login_and_delete(random_credentials)