import requests

def test_oidc_auth():
    client_id = 'your_google_client_id'
    client_secret = 'your_google_client_secret'
    redirect_uri = 'http://localhost'
    code = 'authorization_code_from_previous_step'

    token_url = 'https://oauth2.googleapis.com/token'
    data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    response = requests.post(token_url, data=data)

    assert response.status_code == 200
    token_data = response.json()
    assert 'access_token' in token_data
    assert 'id_token' in token_data

    # Now use the access token to get user info
    access_token = token_data.get('access_token')
    user_info_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
    headers = {'Authorization': f'Bearer {access_token}'}
    user_info = requests.get(user_info_url, headers=headers)

    assert user_info.status_code == 200
    assert 'sub' in user_info.json()  # 'sub' is the user ID in the OpenID Connect response
