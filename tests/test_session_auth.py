import requests

def test_session_auth():
    login_url = 'https://httpbin.org/post'
    login_data = {'username': 'your_username', 'password': 'your_password'}

    session = requests.Session()
    response = session.post(login_url, data=login_data)

    assert response.status_code == 200

    # After login, use the session for subsequent requests
    api_url = 'https://httpbin.org/cookies'
    response = session.get(api_url)

    assert response.status_code == 200
    assert 'cookies' in response.json()
