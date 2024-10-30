В данном проекте тестируется API сайта https://qa-scooter.praktikum-services.ru/
Тестируются следующие сценарии (положительные и отрицательные):
1. Создание курьера
2. Логин курьера
3. Удаление курьера
4. Создание заказа
5. Просмотр всех заказов

Использовались инструменты:
фреймворк - Pytest
отчеты - Allure
API запросы - библиотека requests

Структура проекта:.
├── allure_reports
├── allure_reports.tar
├── chto_testirovat
├── conftest.py
├── data.py
├── helper.py
├── methods
│   ├── courier_methods.py
│   ├── order_methods.py
├── README.md
├── requirements.txt
└── tests
    ├── courier
    │   ├── test_courier_delete.py
    │   ├── test_courier_post_creation.py
    │   └── test_courier_post_login.py
    ├── orders
        ├── test_orders_get.py
        └── test_orders_post.py

