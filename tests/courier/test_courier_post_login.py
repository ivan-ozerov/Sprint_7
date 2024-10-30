from data import URLs
from data import TestData
from methods.courier_methods import CourierMethods
import allure
import pytest
import re

class TestCourierPostLogin:

    @allure.title("Логин курьера с зарегистрированными корректными данными")
    @allure.description("Проверка логина курьера с зарегистрированными корректными данными")
    def test_login_courier__existing_courier_correct_credentials(self, courier):
        response = CourierMethods.courier_login(courier)
        assert response.status_code == 200 and type(response.json()['id']) == int and re.search("^[0-9]+$", str(response.json()['id']))

    @allure.title("Логин курьера с некорректными данными")
    @allure.description("Проверка логина курьера с некорректными данными")
    @pytest.mark.parametrize('field_name', ['password', 'login'])
    def test_login_courier__incorrect_credentials(self, field_name, courier):
        courier_copy = courier.copy()
        courier_copy[field_name] = courier[field_name] + '_new_value'
        response = CourierMethods.courier_login(courier_copy)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Учетная запись не найдена"}

    @allure.title("Логин курьера с отсутствующим полем")
    @allure.description("Проверка логина курьера с отсутствующим полем")
    @pytest.mark.parametrize('field_name', ['login', 'password'])
    def test_login_courier__invalid_credentials__one_field_missed(self, field_name, courier):
        courier_copy = courier.copy()
        del courier_copy[field_name]
        response = CourierMethods.courier_login(courier_copy)
        assert response.status_code == 400 and response.json() == {'code': 400, "message":  "Недостаточно данных для входа"}

    @allure.title("Логин курьера с некорректным типом данных")
    @allure.description("Проверка логина курьера с некорректным типом данных")
    @pytest.mark.parametrize('field_name', ['login', 'password'])
    def test_login_courier__invalid_credentials__one_field_value_wrong_type(self, field_name, courier):
        courier_copy = courier.copy()
        courier_copy[field_name] = 1234
        response = CourierMethods.courier_login(courier_copy)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Учетная запись не найдена"}

    @allure.title("Логин курьера с пустым телом запроса")
    @allure.description("Проверка логина курьера с пустым телом запроса")
    def test_login_courier__invalid_credentials__empty_payload(self):
        response = CourierMethods.courier_login({'firstName':None})
        assert response.status_code == 400 and response.json() == {'code': 400, "message":  "Недостаточно данных для входа"}
