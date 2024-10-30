import copy
import requests
import random
import string
from data import TestData
from data import URLs

class Helper:
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    @classmethod
    def register_new_courier_and_return_login_password(cls):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        payload = cls.generate_random_correct_credentials()

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # создаём список, чтобы метод мог его вернуть
        # login_pass = []

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        # if response.status_code == 201:
        #     login_pass.append(payload['login'])
        #     login_pass.append(payload['password'])
        #     login_pass.append(payload[first_name])

        # возвращаем список
        # return login_pass
        if response.status_code == 201:
            return payload
        else:
            return response.text

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

