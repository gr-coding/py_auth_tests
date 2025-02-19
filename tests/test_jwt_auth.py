import pytest
import requests

def test_jwt_auth():
    url = 'url here'
    jwt_token = 'your_jwt_token'  # Replace with your actual JWT token

    headers = {'Authorization': f'Bearer {jwt_token}'}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    