import requests
from data import TestData, URLs
from helper import Helper


class CourierMethods:

    @classmethod
    def courier_create(cls, credentials):
        response = requests.post(URLs.CREATE_COURIER_URL, data=credentials)
        return response
        
    @classmethod
    def courier_login(cls, credentials):
        credentials = Helper.credentials_for_login(credentials)
        response = requests.post(URLs.LOGIN_COURIER_URL, data=credentials)
        return response

    @classmethod
    def courier_delete(cls, payload):
        response = requests.delete(URLs.create_delete_url(payload), data=payload)
        return response
    


    @classmethod
    def courier_login_and_delete(cls, credentials):
        payload = cls.courier_login(credentials).json()
        response = cls.courier_delete(payload)
        return response

