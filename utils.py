from typing import Optional

from librespot.core import Session

global session
session = None

BASE_HEADERS = HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "app-platform": "WebPlayer",
    "Connection": "keep-alive",
    "content-type": "application/json;charset=UTF-8",
    "DNT": "1",
    "Host": "api-partner.spotify.com",
    "Origin": "https://open.spotify.com",
    "Referer": "https://open.spotify.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "spotify-app-version": "1.1.98.597.g7f2ab0d4",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
}
CLIENT_TOKEN = "AADuJdqUH69pl8ULlnKeEKtcKibqkDK8AtcR/wsC6kmeGcuY8/XjAKEpjRkm8d5BGooFwwh7LZgzbB30BXxUwtBj4tOoprhRyXVbHMIgILyRkcaGz8/gL2SfvWzVxhesrlIm30d4VjiYyj6Giefcn37/DfFPlsOps7Ok0hKK/zjpsF4aYpD9xvZg/z/lxj6aFh7x+Mcmc/+n3LMcsSvcjKaPPIY7hhQnv13GMG8y1FVpZpE2te393gNtkRilHhvhsbdXkwC9vH7TE8Zs0nn0hnFaHH+jJhSeYF41QZFy+O+4cg==",


def get_authorized_headers(access_token: Optional[str] = None, client_token: Optional[str] = None):
    '''Returns headers with given access_token and client_token (both optional)'''
    BASE_HEADERS.update('authorization', 'Bearer ' + access_token)
    BASE_HEADERS.update(
        'client-token',
        client_token if client_token is not None else CLIENT_TOKEN
    )
    return BASE_HEADERS


def get_session(username, password):
    '''return a session object for the given username and password'''
    if not session:
        session = Session.Builder().user_pass(
            username=username, password=password
        ).create()
    return session


def get_auth_token(username, password):
    '''get auth token for the given username and password'''
    if not session:
        session = get_session(username, password)
    auth_token = session.tokens().get('user-read-recently-played')
    return auth_token
