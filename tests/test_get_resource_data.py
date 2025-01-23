import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEME
import allure

BASE_URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
NOT_FOUND_RESOURCE = 'api/unknown/23'

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