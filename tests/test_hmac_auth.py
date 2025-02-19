import requests
import hmac
import hashlib
import time

def test_hmac_auth():
    url = 'https://httpbin.org/anything'
    secret_key = b'your_secret_key'
    data = 'your_request_data'

    timestamp = str(int(time.time()))
    message = f'{data}{timestamp}'
    signature = hmac.new(secret_key, message.encode('utf-8'), hashlib.sha256).hexdigest()

    headers = {
        'X-Signature': signature,
        'X-Timestamp': timestamp
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert 'args' in response.json()
