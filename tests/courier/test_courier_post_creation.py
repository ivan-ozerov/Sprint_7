from data import URLs
from data import TestData
from methods.courier_methods import CourierMethods
import allure
import pytest
import re

class TestCourierPostCreation:

    @allure.title("Создание курьера с корректными данными")
    @allure.description("Проверка создания курьера с корректными данными")
    def test_create_courier__correct_credentials(self):
        response = CourierMethods.courier_create(TestData.CORRECT_COURIER_CREDENTIALS)
        if response.status_code == 201:
            CourierMethods.courier_login_and_delete(TestData.CORRECT_COURIER_CREDENTIALS)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title("Создание курьера с уже существующим в системе логином и паролем")
    @allure.description("Проверка создания курьера с данными, которые уже существуют")
    def test_create_courier__already_existed_with_these_credentials(self):
        response = CourierMethods.courier_create(TestData.CORRECT_COURIER_CREDENTIALS)
        assert response.status_code == 201, "Первый пользователь не был создан."
        response = CourierMethods.courier_create(TestData.CORRECT_COURIER_CREDENTIALS)
        assert response.status_code == 409 and response.json() == {"code" : 409, "message": "Этот логин уже используется. Попробуйте другой."}
        CourierMethods.courier_login_and_delete(TestData.CORRECT_COURIER_CREDENTIALS)

    @allure.title("Создание курьера с уже существующим логином и другим паролем")
    @allure.description("Проверка создания курьера с уже существующим логином и другим паролем")
    def test_create_courier__already_existed_with_this_login_other_password(self):
        response = CourierMethods.courier_create(TestData.CORRECT_COURIER_CREDENTIALS)
        assert response.status_code == 201, "Первый пользователь не был создан."
        correct_credentials_changed_password = TestData.CORRECT_COURIER_CREDENTIALS.copy()
        correct_credentials_changed_password['password'] = TestData.CORRECT_COURIER_CREDENTIALS['password'] + '1'
        response = CourierMethods.courier_create(correct_credentials_changed_password)
        assert response.status_code == 409 and response.json() == {"code" : 409, "message": "Этот логин уже используется. Попробуйте другой."}
        CourierMethods.courier_login_and_delete(TestData.CORRECT_COURIER_CREDENTIALS)

    @allure.title("Создание курьера с отсутствующим полем")
    @allure.description("Проверка создания курьера с отсутствующим полем")
    @pytest.mark.parametrize('field_name', ['login', 'password'])
    def test_create_courier__one_field_missed(self, field_name):
        credentials_without_one_field =  TestData.CORRECT_COURIER_CREDENTIALS.copy()
        del credentials_without_one_field[field_name]
        response = CourierMethods.courier_create(credentials_without_one_field)
        assert response.status_code == 400 and response.json() == {'code' : 400, "message": "Недостаточно данных для создания учетной записи"}

