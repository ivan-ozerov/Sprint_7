import copy
import requests
import random
import string
from data import TestData
from data import URLs

class Helper:

    @classmethod
    def generate_random_correct_credentials(cls):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string


            # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

            # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    @classmethod
    def return_data__for_order_create_method(cls):
        order_data_withour_color = copy.deepcopy(TestData.CORRECT_ORDER_DATA)
        del order_data_withour_color['color']
        colors = ["BLACK", "GREY", ["BLACK", "GREY"], []]
        correct_order_data = []
        for color in colors:
            correct_order_data.append({**TestData.CORRECT_ORDER_DATA, **{'color': color}})
        return correct_order_data

    @classmethod
    def credentials_for_login(cls, credentials):
        copy_credentials = credentials.copy()
        del copy_credentials['firstName']
        return copy_credentials

