import requests

def test_oauth_2_0():
    client_id = 'your_github_client_id'
    client_secret = 'your_github_client_secret'
    redirect_uri = 'http://localhost'
    code = 'your_authorization_code'  # This will be obtained after user authorization

      # Scopes requested for this authorization
    requested_scopes = 'repo'  # You can add other scopes like 'gist', 'user', etc.

    url = 'https://github.com/login/oauth/access_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri,
         'grant_type': 'authorization_code',  # Specify the grant type
    }
    response = requests.post(url, data=data, headers={'Accept': 'application/json'})

    assert response.status_code == 200
    assert 'access_token' in response.json()
