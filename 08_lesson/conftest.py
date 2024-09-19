import pytest
import requests
from constants import X_client_URl

@pytest.fixture()
def get_token(username='bloom', password='fire-fairy'):
    login_pass = {'username': username, 'password': password}
    resp_token = requests.post(X_client_URl + '/auth/login', json=login_pass)
    token = resp_token.json()['userToken']
    return token