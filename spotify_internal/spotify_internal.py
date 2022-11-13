from typing import Optional, Union
import urllib3

import requests

from .. import utils


INTERNAL_BASE_URL = 'https://api-partner.spotify.com/pathfinder/v1/'
INTERNAL_URL = 'https://api-partner.spotify.com/pathfinder/v1/query?operationName={operation_name}&variables={variables}'


class SpotifyInternal:
    def __init__(
        self,
        username,
        password,
        session: Optional[Union[requests.Session, bool]] = True,
        timeout: Optional[int] = 5,
        max_retries=3
    ) -> None:
        self.username = username
        self.password = password
        self.session = session
        self.timeout = timeout
        self.max_retries = max_retries
        self._auth = ''

        if isinstance(self.session, requests.Session):
            self.session = session
        else:
            if self.session:
                self._build_session()
            else:
                session = requests.api

    def set_auth(self, auth):
        self._auth = auth

    def __del__(self):
        if isinstance(self.session, requests.Session):
            self.session.close()

    def _build_session(self):
        self._session = requests.Session()
        retry = urllib3.Retry(
            total=self.max_retries,
            connect=None,
            read=False,
            status=self.max_retries,
            backoff_factor=0.4,
            status_forcelist=(429, 500, 502, 503, 504)
        )

        adapter = requests.adapters.HTTPAdapter(max_retries=retry)
        self._session.mount('http://', adapter)
        self._session.mount('https://', adapter)

    def _auth_headers(self):
        if not self._auth:
            self._auth = utils.get_auth_token(self.username, self.password)

        return utils.get_authorized_headers(self._auth)

    def _internal_call(self, method, url):
        if not url.startswith('http://'):
            url = INTERNAL_BASE_URL + url
        headers = self._auth_headers()
        response = self.session.request(
            method,
            url,
            headers=headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        results = response.json()
        return results

    def _get(self, url, params, **kwargs):
        if params:
            kwargs.update(params)
        return self._internal_call('GET', url)

    def search(self, search_term, offset=0, limit=10, no_of_top_results=5):
        operation_name = 'searchDesktop'
        return self._get()


if __name__ == '__main__':
    s = SpotifyInternal("gmadhuri445@gmail.com", "AdItYa123")
