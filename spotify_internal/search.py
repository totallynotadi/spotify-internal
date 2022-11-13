import requests

URL = "https://api-partner.spotify.com/pathfinder/v1/query?operationName=searchDesktop&variables=%7B%22searchTerm%22%3A%22ginger+clap%22%2C%22offset%22%3A0%2C%22limit%22%3A10%2C%22numberOfTopResults%22%3A5%2C%22includeAudiobooks%22%3Afalse%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%221d3a8f81abf4f33f49d1e389ed0956761af669eedb62a050c6c7bce5c66070bb%22%7D%7D"

HEADERS = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en",
    "app-platform": "WebPlayer",
    "authorization": "Bearer BQAm-pCuYt-diR4liM4zkwt7vujM4NqtYWzKVUznSFFierUEbumti_FGaG3889fQpc9_n6tBmhO7hQvvgURVSdeA865jUmBXSCJQg2J6zdpT7iUe9LE",
    "client-token": "AAAdIGsLFOBJ1XdkCtqKedoBdNPWv+ra5HK7GWPLvhZZkQAmT+HoX6bnYPI7AMZHgQN9MAuAEoFypb4BtPNO9wA8njnzDhvPbpsFkSCTssmS+mA8QUA/M6peoT4+O8YUuxyW8tVcYeWYdTj4DLe4RiVArycy4WJszCILjx4FGwTYGnQ9sKdEOOdbX722Lpvd8Y3zLGXVfRygCwcCOqvUBmTfZnOvufUEDg1fFMEg7mMTUgzBKvMuCAr/g7RfGp9XKPLpEg9kTDQsMRuVmN6fw1Fzv7zNf36SKZOWYyIj2Ncv",
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

data = requests.get(URL, headers=HEADERS)
