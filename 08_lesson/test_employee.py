import pytest
import requests
from employee import Company, Employer

company = Company()
employer = Employer()

@pytest.fixture()
def get_token(username='leonardo', password='leads'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post('https://x-clients-be.onrender.com' + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token

def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)


def test_getcompany_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()


def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Olesya',
        'lastName': 'Efremova',
        'middleName': 'string',
        'companyID': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-09-14T11:02:47.622Z',
        'isActive': 'true'
    }
    new_employer_id = (employer.add_new(token, body_employer))['id']
    assert new_employer_id is not None
    assert str(new_employer_id).isdigit()

    info = employer.get_info(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200


def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Internal server error'


def test_get_employer():
    com_id = company.last_active_company_id()
    list_employers = employer.get_list(com_id)
    assert isinstance(list_employers, list)
       

def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
        

def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Olesya',
        'lastName': 'Efremova',
        'middleName': 'string',
        'companyID': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-09-14T11:02:47.622Z',
        'isActive': 'true'    
    }
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'Silaeva',
        'email': 'test2@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200
    assert id == employer_changed.json()['id']
    assert (employer_changed.json()["email"]
            ) == body_change_employer.get("email")

def test_employes_missing_id_and_token():
    try:
        employer.change_info()
    except TypeError as e:
        assert str(
            e) == "Employer.change_info() missing 3 required positional argument: 'token', 'employee_id', and 'body'"
