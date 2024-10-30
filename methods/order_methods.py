import requests
from data import URLs
import helper

class OrderMethods:

    @classmethod
    def order_create(cls, order_data):
        response = requests.post(URLs.CREATE_ORDER_URL, params=order_data)
        return response
    
    @classmethod
    def get_orders_list(cls, orders_list_params=None):
        response = requests.get(URLs.GET_ORDER_LIST_URL, params=orders_list_params)
        return response