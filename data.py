
class URLs:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = MAIN_URL + '/api/v1/courier'
    LOGIN_COURIER_URL = MAIN_URL + '/api/v1/courier/login'
    CREATE_ORDER_URL = MAIN_URL + '/api/v1/orders'
    GET_ORDER_LIST_URL = MAIN_URL + '/api/v1/orders'
    GET_DELETE_URL = MAIN_URL + '/api/v1/courier'


    @classmethod
    def create_delete_url(cls, payload):
        return f'{cls.MAIN_URL}/api/v1/courier/{payload["id"]}'

class TestData:
    
    CORRECT_COURIER_CREDENTIALS = {
        "login": "kringe_champion",
        "password": "1234",
        "firstName": "Ivan"
    }

    CORRECT_ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    INVALID_DATA_FOR_DELETE = [
            {'id' : ''},
            {'id' : 'wrong_id_type'}
        ]

print(TestData.CORRECT_COURIER_CREDENTIALS)