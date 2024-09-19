import pytest
import requests
from employee import Company, Employee

employer = Employee()
company = Company()


def test_authoriazation(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token,str)

def test_get_company_id():
    company_id = company.last_active_company()
    assert company_id is not None
    assert str(company_id).isdigit()    

def test_add_employer(get_token):
    token = str(get_token)
    comp_id = company.last_active_company()
    body_employer = {
        'id': 0,
        'firstName': 'Olesya',
        'lastName': 'Efrmova',
        'middleName': 'Lesy',
        'companyId': comp_id,
        'email': 'olesya89@gmail.com',
        'url': 'string',
        'phone': '+79288119107',
        'birthdate': '2024-09-04T17:57:37.050Z',
        'isActive': True
    }
    new_employer_id = employer.add_employee_into_company(token, body_employer)['id']
    assert new_employer_id is not None
    assert len(body_employer)==10
    assert str(new_employer_id).isdigit()    

    #Получаем инфо о добавленном сотруднике
    info = employer.get_info_for_employee(new_employer_id)
    assert info.json()['id']== new_employer_id
    assert info.status_code == 200

# Проверка невозможности создания сотрудника без токена

def test_add_employer_without_token():
    comp_id = company.last_active_company()
    token =""
    body_employer = {
        'id': 0,
        'firstName': 'Olesya',
        'lastName': 'Efremova',
        'middleName': 'Lesy',
        'companyId': comp_id,
        'email': 'olesya89@gmail.com',
        'url': 'string',
        'phone': '+79288119107',
        'birthdate': '2024-09-04T17:57:37.050Z',
        'isActive': True
    }
    new_employer = employer.add_employee_into_company(token,body_employer)
    assert new_employer['message'] == 'Unauthorized'

# Проверяем создание клиента без тела запроса
def test_add_employer_without_body(get_token):
    comp_id = company.last_active_company()
    token = str(get_token)
    body_employer = {}
    new_employer = employer.add_employee_into_company(token, body_employer)
    assert new_employer['message'] == 'Internal server error'

def test_get_employer():
    com_id = company.last_active_company()

    # Получаем список работников конкретной компании
    list_employers = employer.get_list_employee_company(com_id)

    # Проверяем что нам вернулся список []
    assert isinstance(list_employers,list)

    # Проверяем обязательное поле "ID company"в запросе списка на получение раьотников без указания "ID company"
def test_get_list_employer_wuthout_company_id():
    try:
        employer.get_list_employee_company()
    except TypeError as x:
        assert str(x) == "Employee.get_list_employee_company() missing 1 required positional argument: 'company_id'"
