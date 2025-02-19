import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    url = 'https://httpbin.org/basic-auth/user/pass'
    username = 'user'
    password = 'pass'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    assert response.status_code == 200
    assert response.json()['authenticated'] is True
