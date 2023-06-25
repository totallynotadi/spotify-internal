import json
import time
from dataclasses import dataclass, field

from spotify_internal import login

__all__ = [
    'Tokens',
    'Credentials',
    'prepare_url',
    'INTERNAL_BASE_URL',
    'INTERNAL_URL'
]


INTERNAL_BASE_URL = 'https://api-partner.spotify.com/pathfinder/v1/query'
INTERNAL_URL = 'https://api-partner.spotify.com/pathfinder/v1/query?operationName=%(operation_name)s&variables=%(variables)s&extensions={"persistedQuery":{"version":1,"sha256Hash":"%(hash)s"}}'


@dataclass
class Credentials:
    username: str
    password: str

    def get_tokens(self) -> "Tokens":
        Tokens.from_creds(self)


@dataclass
class Tokens:
    access_token: str
    client_token: str = field(default="AADHU245K/LDrxWbEFzVu/6SXnvisFYKHWL/5GOArj4t0pova2MSLooib1A6y+nzd6rbWeoMBX1/3TA1rDCWm8hHNZTGxGbcns93k9AfquPGSAkCbEOfaFGyMeHhm28qPSG8XGyGdHJLivFfeI7wfnlsQat7GtFkB4HhEoiX4+3sSLUtt2Yks/Ruh9MUialJI2nyhHLA5jHDivKJdNPeq402VW4PaK3kF2E0qMyg+abRdyeNpc165vJcE69ZiF+CI7gsIayKRK2gYjxi502F55Zclj/LZIxvhUgRJ1hj9WKa93eYCw==", init=False)
    # client_token: str = field(default="AAC1RsZCX0+3l2nT64BOm/RaAnqAU5sNIuh4D0eQuPi/e2oZFDgCi9fjGIPO2bP6hQZdhvlqEn3m11RWjUZ6kKXP2i9Bph1eXjPwOwvg2NDo5Dt7Zepb/PaXk/YKR7hxItBtTT4I95x0iLkCXPbnd8dIA9ossSljQYpoENq8YTNWgycyzsu/aV7SD+XY75E0flNzn6X3tGHgOkEI8RjGb5pqjTVStfzp22y87PvHDfH45H01hhGij3ph3fgCbT3nEZYH0qQ1/9opmheHnayXyP5igL9Ta7buSyfSEhe821BOCgok=", init=False)

    def __post_init__(self):
        object.__setattr__(self, 'expires_at', (int(time.time()) + 3600) - 10)

    @classmethod
    def from_credentials(cls, credentials: Credentials) -> "Tokens":
        return cls(login.get_auth_token(credentials))


def hash(endpoint: dict):
    return endpoint['extensions']['persistedQuery']['sha256Hash']


def prepare_url(operation_name: str, variables: dict, hash: str):
    url = INTERNAL_URL % {'operation_name': operation_name,
                          'variables': json.dumps(variables),
                          'hash': hash}
    url = url.replace(' ', '').replace("'", '"')
    return url


if __name__ == '__main__':
    tokens = Tokens.lmao('sadfa')
    print(tokens.client_token)
    print(tokens.expires_at)
