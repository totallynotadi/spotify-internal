import requests

URL = 'https://api-partner.spotify.com/pathfinder/v1/query?operationName=fetchExtractedColors&variables={{"uris":["{image_url}"]}}&extensions={{"persistedQuery":{{"version":1,"sha256Hash":"d7696dd106f3c84a1f3ca37225a1de292e66a2d5aced37a66632585eeb3bbbfa"}}}}'
HEADERS = {
    'name': 'User-Agent',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en',
    'app-platform': 'WebPlayer',
    'authorization': 'Bearer BQB7R8ZZISLKeUi4mNjpPp9Ffmea2s98vRwvbPQcYykB_hX83I-zQXy0fU6eUA-zHqeMv9W-ewAqx0cS9NvpiRtHkSXj4-3CJOhyiYJB0nSbS5sbsCsOP8irPlcSpQTpy1GaOJn_WUBDosKqpuvGU-CqGqZxbT6ArLgRWBHElQXmYvvonLCCH_D5iDDyNUVTNIMmtauHpvXT1mWCk8MBe_QkVZNVqIlbJdZDJ-yEfh4KBhsghQKiZN_PbKrq',
    # 'client-token': 'AADuJdqUH69pl8ULlnKeEKtcKibqkDK8AtcR/wsC6kmeGcuY8/XjAKEpjRkm8d5BGooFwwh7LZgzbB30BXxUwtBj4tOoprhRyXVbHMIgILyRkcaGz8/gL2SfvWzVxhesrlIm30d4VjiYyj6Giefcn37/DfFPlsOps7Ok0hKK/zjpsF4aYpD9xvZg/z/lxj6aFh7x+Mcmc/+n3LMcsSvcjKaPPIY7hhQnv13GMG8y1FVpZpE2te393gNtkRilHhvhsbdXkwC9vH7TE8Zs0nn0hnFaHH+jJhSeYF41QZFy+O+4cg==',
    'Connection': 'keep-alive',
    'content-type': 'application/json;charset=UTF-8',
    'DNT': '1',
    'Host': 'api-partner.spotify.com',
    'Origin': 'https://open.spotify.com',
    'Referer': 'https://open.spotify.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'spotify-app-version': '1.1.97.57.g973f7e33',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}

image_url = 'https://i.scdn.co/image/ab67616d0000b27342ecfc452acc4d6659513b34'
final_url = URL.format(image_url=image_url)
data = requests.get(final_url, headers=HEADERS, timeout=10)
print(data)
# data = data.json()
# colors = data['data']['extractedColors'][0]
# print(colors['colorRaw']['hex'], colors['colorDark']['hex'])
