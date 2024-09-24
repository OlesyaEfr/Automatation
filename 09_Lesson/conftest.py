import pytest
import requests

@pytest.fixture()
def get_token(username='bloom', password='fire-fairy'):
    login_pass = {'username': username, 'password': password}
    resp_token = requests.post('https://x-clients-be.onrender.com' + '/auth/login', json=login_pass)
    token = resp_token.json()['userToken']
    return token
