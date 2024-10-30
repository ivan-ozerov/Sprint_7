import allure
import re
import pytest
import requests
from data import TestData
from methods.order_methods import OrderMethods


class TestOrdersGet:

    @allure.title("Получение всего списка заказов")
    @allure.description("Проверка получения всего списка заказов")
    def test_get_orders_list(self):
        response = OrderMethods.order_create(TestData.CORRECT_ORDER_DATA)
        response = OrderMethods.get_orders_list()
        assert response.status_code == 200 and response.json()['orders']