from typing import Literal, Optional, Union

import requests
import urllib3
import spotipy
# from melodine import ytmusic

from spotify_internal import login
from spotify_internal import utils
from spotify_internal.endpoints import endpoints
# from spotify_internal.utils import Tokens, prepare_url


class SpotifyInternal:
    def __init__(
        self,
        username,
        password,
        session: Optional[Union[requests.Session, bool]] = True,
        timeout: Optional[int] = 5,
        max_retries=3
    ) -> "SpotifyInternal":
        self._session = session
        self.timeout = timeout
        self.max_retries = max_retries

        # user creds
        self.credentials: utils.Credentials = utils.Credentials(
            username, password)
        # spotify auth tokens
        self._auth: utils.Tokens = utils.Tokens.from_credentials(
            self.credentials)
        self.spotify = spotipy.Spotify(self._auth.access_token)

        if isinstance(self._session, requests.Session):
            self._session = session
        else:
            if self._session:
                self._build_session()
            else:
                self._session = requests.api

    def set_auth(self, auth: Union[str, utils.Credentials]) -> None:
        if isinstance(auth, str):
            auth = utils.Credentials(auth)
        self._auth = auth

    def __del__(self):
        if isinstance(self._session, requests.Session):
            self._session.close()

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
            self._auth = utils.Tokens(login.get_auth_token(self.credentials))

        return login.get_authorized_headers(self._auth)

    def _internal_call(self, method: Literal['GET', 'POST', 'UPDATE', 'DELETE'], url: str, payload: Optional[dict] = None, query_params=None):
        headers = self._auth_headers()
        response = self._session.request(
            method,
            url,
            headers=headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        results = response.json()
        return results

    def _get(self, url, payload: Optional[dict] = None, **kwargs):
        if payload:
            kwargs.update(payload)
        return self._internal_call('GET', url, payload, kwargs)

    def browse_all(self, limit=99, offset=0):
        operation_name = 'browseAll'
        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        print(variables)
        variables['sectionPagination']['limit'] = limit
        variables['sectionPagination']['offset'] = offset
        hash = endpoint['extensions']['persistedQuery']['sha256Hash']
        url = utils.prepare_url(operation_name, variables, hash)
        return self._get(url)['data']['browseStart']['sections']['items'][0]['sectionItems']['items']

    def browse_section(self, section: str, limit=20, offset=0):
        if not section.startswith('spotify:section:'):
            section = 'spotify:section:' + section
        operation_name = 'browseSection'
        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        print(variables)
        variables['pagination']['limit'] = limit
        variables['pagination']['offset'] = offset
        variables['uri'] = section
        hash = endpoint['extensions']['persistedQuery']['sha256Hash']
        url = utils.prepare_url(operation_name, variables, hash)
        return self._get(url)['data']

    def browse_page(self, page: str, limit=20, offset=0):
        operation_name = 'browsePage'
        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        variables['sectionPagination']['limit'] = limit
        variables['sectionPagination']['offset'] = offset
        variables['uri'] = page
        hash = endpoint['extensions']['persistedQuery']['sha256Hash']
        url = utils.prepare_url(operation_name, variables, hash)
        return self._get(url)['data']

    def home(self):
        operation_name = 'home'
        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        hash = endpoint['extensions']['persistedQuery']['sha256Hash']
        url = utils.prepare_url(operation_name, variables, hash)
        return self._get(url)['data']['home']

    def home_section(self, section: str):
        if not section.startswith('spotify:section:'):
            section = 'spotify:section:' + section
        operation_name = 'homeSection'
        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        variables['uri'] = section
        hash = endpoint['extensions']['persistedQuery']['sha256Hash']
        url = utils.prepare_url(operation_name, variables, hash)
        return self._get(url)['data']

    def search(self, search_term, offset=0, limit=10, no_of_top_results=5):
        operation_name = 'searchDesktop'

        endpoint = endpoints[operation_name]
        # variables = endpoint['variables']
        variables = {
            'searchTerm': search_term,
            'offset': offset,
            'limit': limit,
            'numberOfTopResults': no_of_top_results,
            'includeAudiobooks': True
        }
        url = utils.prepare_url(
            operation_name, variables, utils.hash(endpoint))
        # return self._get(url)['data']['searchV2']
        return self._get(url)

    def library_tracks(self, limit=20, offset=0):
        operation_name = 'fetchLibraryTracks'

        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        variables['limit'] = limit
        variables['offset'] = offset
        url = utils.prepare_url(
            operation_name, variables, utils.hash(endpoint))
        return self._get(url)['data']['me']['library']

    def playlist(self, playlist_id: str):
        # decoratePlaylists&variables={"uris":["spotify:playlist:4O37Nstn92l8KVJhxme05s"]}
        # operation_name = 'decoratePlaylists'

        # endpoint = endpoints[operation_name]
        # variables = endpoint['variables']
        # variables['uris']
        # variables = {"uris": [f"spotify:playlist:{playlist_id}"]}
        # url = utils.prepare_url(
        #     operation_name, variables, utils.hash(endpoint))
        # return self._get(url)
        return self.spotify.playlist(playlist_id)

    def user(self, user_id: str):
        return self.spotify.user(user_id)

    def get_color(self, image_url: str):
        # fetchExtractedColors&variables={"uris":["https://i.scdn.co/image/ab67706f000000034f1883bcac8e10d210f69d7f"]}
        operation_name = 'fetchExtractedColors'

        endpoint = endpoints[operation_name]
        variables = endpoint['variables']
        variables = {'uris': [image_url]}
        url = utils.prepare_url(
            operation_name, variables, utils.hash(endpoint))
        return self._get(url)['data']

    def track_name_from_id(self, track_id: str):
        track_data = self.spotify.track(track_id)
        # track = ytmusic.search(f"{track_data['artists'][0]['name']} - {track_data['name']}").tracks[0]
        # url = track.url
        return f"{track_data['artists'][0]['name']} - {track_data['name']}"

    def get_lyrics(self):
        url = 'https://spclient.wg.spotify.com/color-lyrics/v2/track/22L7bfCiAkJo5xGSQgmiIO/image/spotify:image:ab67616d0000b273d9194aa18fa4c9362b47464f?clientLanguage=en'
        return self._get(url)
