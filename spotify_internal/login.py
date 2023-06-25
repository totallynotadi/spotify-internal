
from librespot.core import Session

from spotify_internal.utils import Credentials, Tokens

global session
session = None

BASE_HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "app-platform": "WebPlayer",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "content-type": "application/json;charset=UTF-8",
    "DNT": "1",
    "Host": "api-partner.spotify.com",
    "Origin": "https://open.spotify.com",
    "Pragma": "no-cache",
    "Referer": "https://open.spotify.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "spotify-app-version": "1.1.99.2454.ga8809a84",
    "TE": "trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
}


def get_authorized_headers(tokens: Tokens) -> dict:
    '''Returns headers with given access_token and client_token (both optional)'''
    auth_headers = BASE_HEADERS.copy()
    auth_headers.update({'authorization': 'Bearer ' + tokens.access_token})
    # auth_headers.update({'client-token': tokens.client_token})
    return auth_headers


def get_session(credentials: Credentials):
    '''return a session object for the given username and password'''
    global session
    if not session:
        session = Session.Builder().user_pass(
            username=credentials.username,
            password=credentials.password
        ).create()
    return session


def get_auth_token(credentials: Credentials):
    '''get auth token for the given username and password'''
    global session
    if not session:
        session = get_session(credentials)
    auth_token = session.tokens().get('user-read-recently-played')
    return auth_token
