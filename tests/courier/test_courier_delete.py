from data import URLs
from data import TestData
from helper import Helper
from methods.courier_methods import CourierMethods
import pytest

class TestCourierDelete:

    def test_delete_courier__existed_user(self):
        response_create = CourierMethods.courier_create(TestData.CORRECT_COURIER_CREDENTIALS)
        response = CourierMethods.courier_login_and_delete(TestData.CORRECT_COURIER_CREDENTIALS)
        response = CourierMethods.courier_login(TestData.CORRECT_COURIER_CREDENTIALS)
        assert response.status_code == 404 and response.json() == {'code' : 404, "message": "Учетная запись не найдена"}
        
    def test_delete_courier__not_existed_courier(self):
        response_create = CourierMethods.courier_create(TestData.CORRECT_COURIER_CREDENTIALS)
        response_login = CourierMethods.courier_login(TestData.CORRECT_COURIER_CREDENTIALS)
        response = CourierMethods.courier_delete({"id": (response_login.json()['id'] + 10)})
        response = CourierMethods.courier_delete({"id": response_login.json()['id']})
        assert response.status_code == 200 and response.json() == {'ok': True}

    def test_delete_courier__empty_id(self):
        response = CourierMethods.courier_delete(TestData.INVALID_DATA_FOR_DELETE[0])
        assert response.status_code == 404 and response.json() == {"code": 404, "message": "Not Found."}


    def test_delete_courier__invalid_type_id(self):
        response = CourierMethods.courier_delete(TestData.INVALID_DATA_FOR_DELETE[1])
        assert response.status_code == 500 and response.json() == {'code' : 500, "message":  'invalid input syntax for type integer: "wrong_id_type"'}
