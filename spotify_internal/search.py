import requests

from spotify_internal import utils

URL = "https://api-partner.spotify.com/pathfinder/v1/query?operationName=searchDesktop&variables=%7B%22searchTerm%22%3A%22ginger+clap%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22numberOfTopResults%22%3A5%2C%22includeAudiobooks%22%3Afalse%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%221d3a8f81abf4f33f49d1e389ed0956761af669eedb62a050c6c7bce5c66070bb%22%7D%7D"
HEADERS = utils.get_authorized_headers()

data = requests.get(URL, headers=HEADERS)
