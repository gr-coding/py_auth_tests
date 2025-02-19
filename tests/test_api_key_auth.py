import requests

def test_api_key_auth():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    city = 'London'
    api_key = 'your_openweathermap_api_key'  # Replace with your actual API key

    params = {'q': city, 'appid': api_key}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert 'weather' in response.json()