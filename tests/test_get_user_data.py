import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEME, RESOURCE_DATA_SCHEME
import allure

BASE_URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
LIST_RESOURCE = 'api/unknown'
SINGLE_USER = 'api/users/2'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_USER = 'api/users/23'
NOT_FOUND_RESOURCE = 'api/unknown/23'
EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEME)
            with allure.step('Проверяем окончание Email адреса'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step('Проверяем наличие id в ссылке на аватарку'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение единственного пользователя')
def test_single_user():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    with allure.step('Проверяем окончание Email адреса'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем наличие id в ссылке на аватарку'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)

@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем отсутствие пользователя')
def test_user_not_found():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + NOT_FOUND_USER}'):
        response = httpx.get(BASE_URL + NOT_FOUND_USER)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение списка ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    data = response.json()['data']
    for item in data:
        with allure.step('Проверяем элемент из списка'):
            validate(item, RESOURCE_DATA_SCHEME)
            with allure.step('Проверяем наличие # в цвете'):
                assert item['color'].startswith('#')
            with allure.step('Проверяем наличие разделителя в pantone_value'):
                assert '-' in item['pantone_value']

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем получение единственного ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert  response.status_code == 200

    data = response.json()['data']
    with allure.step('Проверяем наличие # в цвете'):
        assert data['color'].startswith('#')
    with allure.step('Проверяем наличие разделителя в pantone_value'):
        assert '-' in data['pantone_value']

@allure.suite('Проверка запросов данных ресурсов')
@allure.title('Проверяем отсутствие ресурса')
def test_resource_not_found():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + NOT_FOUND_RESOURCE}'):
        response = httpx.get(BASE_URL + NOT_FOUND_RESOURCE)
    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404