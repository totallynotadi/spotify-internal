
import time
import requests

from .config import sp_dc, sp_key


ACCESS_TOKEN_URL = 'https://open.spotify.com/get_access_token?reason=transport&productType=web_player'
ACCESS_TOKEN_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'cookie': f'sp_dc={sp_dc};sp_key={sp_key};'
}

CLIENT_TOKEN_URL = 'https://clienttoken.spotify.com/v1/clienttoken'
CLIENT_TOKEN_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
CLIENT_TOKEN_PAYLOAD = {
    'client_data': {
        'client_id': 'f6a40776580943a7bc5173125a1e8832',
        'client_version': '1.1.97.136.g81a082e9',
        'js_sdk_data': {
            'device_brand': "unknown",
            'device_model': "desktop",
            'os': "Linux",
            'os_version': "unknown"
        }
    }
}


def get_access_token():
    access_token_data = requests.get(
        ACCESS_TOKEN_URL, ACCESS_TOKEN_HEADERS).json()
    client_id = access_token_data['clientId']
    access_token = access_token_data['accessToken']
    expires_at = access_token_data['accessTokenExpirationTimestampMs'] // 1000
    return {'token': access_token, 'client_id': client_id, 'expires_at': expires_at}


def get_client_token():
    client_token_data = requests.post(
        CLIENT_TOKEN_URL, json=CLIENT_TOKEN_PAYLOAD, headers=CLIENT_TOKEN_HEADERS).json()
    client_token = client_token_data['granted_token']['token']
    expires_at = int(time.time()) + \
        client_token_data['granted_token']['refresh_after_seconds']
    return {'token': client_token, 'expires_at': expires_at}


def get_client_id():
    return get_access_token()['client_id']


def get_auth_params():
    access_token = get_access_token()
    client_token = get_client_token()
    return {'access_token': access_token, 'client_token': client_token}


if __name__ == '__main__':
    print(get_access_token())
    print()
    print(get_client_token())
