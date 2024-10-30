import allure
import re
import pytest
import requests
from data import TestData
from helper import Helper
from methods.order_methods import OrderMethods




class TestOrdersPost:

    @allure.title("Создание заказов с различными цветами")
    @allure.description("Проверка создания заказов с различными цветами")
    @pytest.mark.parametrize('order_data', Helper.return_data__for_order_create_method())
    def test_create_order__correct_data__various_colors(self, order_data):
        response = OrderMethods.order_create(order_data)
        assert response.status_code == 201 and type(response.json()['track']) == int and re.search("^[0-9]+$", str(response.json()['track']))
