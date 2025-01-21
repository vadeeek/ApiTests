import allure
import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME, UPDATED_USER_SCHEME
import datetime

BASE_URL = 'https://reqres.in/'
CREATE_USER = 'api/users'
UPDATE_USER = 'api/users/2'
DELETE_USER = 'api/users/2'

@allure.suite('Проверка создания пользователей')
@allure.title('Проверка создания пользователя с именем и работой')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step(f'Проверяем имя пользователя'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем работу пользователя'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания пользователей')
@allure.title('Проверка создания пользователя без имени')
def test_create_user_without_name():
    body = {
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step(f'Проверяем работу пользователя'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка создания пользователей')
@allure.title('Проверка создания пользователя без работы')
def test_create_user_without_job():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + CREATE_USER}'):
        response = httpx.post(BASE_URL + CREATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 201

    response_json = response.json()
    creation_date = response_json['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step(f'Проверяем имя пользователя'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка обновления пользователей (PUT)')
@allure.title('Проверка обновления пользователя с именем и работой')
def test_update_user_with_name_and_job_put():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_USER}'):
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step(f'Проверяем имя пользователя'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем работу пользователя'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка обновления пользователей (PUT)')
@allure.title('Проверка обновления пользователя без имени')
def test_update_user_without_name_put():
    body = {
        "job": "zion resident"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_USER}'):
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step(f'Проверяем работу пользователя'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка обновления пользователей (PUT)')
@allure.title('Проверка обновления пользователя без работы')
def test_update_user_without_job_put():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_USER}'):
        response = httpx.put(BASE_URL + UPDATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step(f'Проверяем имя пользователя'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка обновления пользователей (PATCH)')
@allure.title('Проверка обновления пользователя с именем и работой')
def test_update_user_with_name_and_job_patch():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_USER}'):
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step(f'Проверяем имя пользователя'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем работу пользователя'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка обновления пользователей (PATCH)')
@allure.title('Проверка обновления пользователя без имени')
def test_update_user_without_name_patch():
    body = {
        "job": "zion resident"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_USER}'):
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step(f'Проверяем работу пользователя'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка обновления пользователей (PATCH)')
@allure.title('Проверка обновления пользователя без работы')
def test_update_user_without_job_patch():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Делаем запрос по адресу {BASE_URL + UPDATE_USER}'):
        response = httpx.patch(BASE_URL + UPDATE_USER, json=body)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    response_json = response.json()
    creation_date = response_json['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.now(datetime.UTC))

    with allure.step('Валидация схемы ответа'):
        validate(response_json, UPDATED_USER_SCHEME)
    with allure.step(f'Проверяем имя пользователя'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем корректность времени создания пользователя'):
        assert creation_date[0:16] == current_date[0:16]

@allure.suite('Проверка удаления пользователей')
@allure.title('Проверка удаления пользователя')
def test_delete_user():
    with allure.step(f'Делаем запрос по адресу {BASE_URL + DELETE_USER}'):
        response = httpx.delete(BASE_URL + DELETE_USER)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 204