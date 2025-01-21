import json
import httpx
import pytest
import allure
from jsonschema import validate
from core.contracts import SUCCESSFUL_REGISTERED_USER_SCHEME, \
    UNSUCCESSFUL_REGISTERED_USER_SCHEME, SUCCESSFUL_LOGIN_USER_SCHEME, UNSUCCESSFUL_LOGIN_USER_SCHEME

BASE_URL = 'https://reqres.in/'
REGISTER_USER = 'api/register'
LOGIN_USER = 'api/login'

new_users_json_file = open('/Users/Velichko.Vadim4/PycharmProjects/ApiTests/core/new_users_data.json')
new_users_data = json.load(new_users_json_file)

login_users_json_file = open('/Users/Velichko.Vadim4/PycharmProjects/ApiTests/core/login_users_data.json')
login_users_data = json.load(login_users_json_file)

@allure.suite('Проверка регистрации')
@allure.title('Проверка успешной регистрации')
@pytest.mark.parametrize('new_users_data', new_users_data)
def test_successful_register(new_users_data):
    with allure.step(f'Делаем запрос по адресу {BASE_URL + REGISTER_USER}'):
        response = httpx.post(BASE_URL + REGISTER_USER, json=new_users_data)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step('Валидация схемы ответа'):
        validate(response.json(), SUCCESSFUL_REGISTERED_USER_SCHEME)

@allure.suite('Проверка регистрации')
@allure.title('Проверка неуспешной регистрации')
def test_unsuccessful_register():
    body = {
        "email": "sydney@fife"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + REGISTER_USER}'):
        response = httpx.post(BASE_URL + REGISTER_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 400

    response_json = response.json()

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UNSUCCESSFUL_REGISTERED_USER_SCHEME)

@allure.suite('Проверка логина')
@allure.title('Проверка успешного логина')
@pytest.mark.parametrize('login_users_data', login_users_data)
def test_successful_login(login_users_data):
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LOGIN_USER}'):
        response = httpx.post(BASE_URL + LOGIN_USER, json=login_users_data)
    with allure.step(f'Проверяем код ответа'):
        assert  response.status_code == 200

    with allure.step('Валидация схемы ответа'):
        validate(response.json(), SUCCESSFUL_LOGIN_USER_SCHEME)

@allure.suite('Проверка логина')
@allure.title('Проверка неуспешного логина')
def test_unsuccessful_login():
    body = {
        "email": "peter@klaven"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LOGIN_USER}'):
        response = httpx.post(BASE_URL + LOGIN_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 400

    response_json = response.json()

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UNSUCCESSFUL_LOGIN_USER_SCHEME)