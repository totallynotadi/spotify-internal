endpoints = {
    "fetchLibraryEpisodes": {
        "method": "GET",
        "variables": {
            "offset": 0,
            "limit": 1
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "9e29327f894fd53aff9f67f108aa567894750a50bb132245b12818a0c2f39296"
            }
        }
    },
    "home": {
        "method": "GET",
        "variables": {
            "timeZone": "Asia/Kolkata"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "3a67ee0ea6abad2ebad2e588a9aa130fc98d6b553f5b05ac6467503d02133bdc"
            }
        }
    },
    "decorateContextTracks": {
        "method": "GET",
        "variables": {
            "uris": [
                "spotify:track:2enPRFda84VE2wtI8c86Uf",
                "spotify:track:0wtvpspGErTrF9BRqVdHVF",
                "spotify:track:086myS9r57YsLbJpU0TgK9",
                "spotify:track:47Cm89ETWsOrxtArDnYyrf",
                "spotify:track:130dsYbbXp9jQnETiJ7axI",
                "spotify:track:7DCEo0VsBRC4YO0L01EMZw",
                "spotify:track:3Wrjm47oTz2sjIgck11l5e",
                "spotify:track:02HNBwIheiZAuzC8p1QBPn",
                "spotify:track:3AVrVz5rK8Hrqo9YGiVGN5",
                "spotify:track:0HUTL8i4y4MiGCPId7M7wb",
                "spotify:track:6Qu0JNnXdUOGtTVwuFVeJy",
                "spotify:track:6HWH450jaQi27kwtR6Ffum",
                "spotify:track:51aWYPDZOfvZxkvoDWfYwn",
                "spotify:track:4XfI7M5gLwEY84gYiH4RDD",
                "spotify:track:6405hOm4Nxfxzm2wxXw2BU",
                "spotify:track:3LGsgpx4TfxhXbr07OFKqs",
                "spotify:track:1H7zdcRD0gLGQY0w5ejGgX",
                "spotify:track:4KcCRwvfNEdLShOdkEOxCA",
                "spotify:track:1G4ylW7bDwQ1mWeIHHGBhV",
                "spotify:track:2sI0Geda1N0cAjKnbzujHs"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "d4e07a4541bb7594ce30a2eeaaf35a2d78733ef59d0f5c88bdf3dcc2579dc0b6"
            }
        }
    },
    "fetchPlaylistForRecentlyPlayed": {
        "method": "GET",
        "variables": {
            "uri": "spotify:playlist:7116NaHo5yygkAjoBmLaIq"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "357c4bb9f0dcce45dfee3f99371f79c9abec57c274a795bcdfd6050f07a63dde"
            }
        }
    },
    "fetchLibraryTracks": {
        "method": "GET",
        "variables": {
            "offset": 0,
            "limit": 1
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "8474ec383b530ce3e54611fca2d8e3da57ef5612877838b8dbf00bd9fc692dfb"
            }
        }
    },
    "areAlbumsInLibrary": {
        "method": "GET",
        "variables": {
            "uris": [
                "spotify:album:3FZtDulD5KUnIxA9dM1v5M",
                "spotify:album:3nCBCXR2ZCmlHojlykcB3S"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "eb48a7089227861e1df67e3c1bd625cfa55572d3c1eebe7e4d35deca14251f2c"
            }
        }
    },
    "areTracksInLibrary": {
        "method": "GET",
        "variables": {
            "uris": [
                "spotify:track:2enPRFda84VE2wtI8c86Uf"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "2b51d510cac8d1262d8ed3d44af70e45a41b3c4d94c454483e779dcae6dc890e"
            }
        }
    },
    "browseAll": {
        "method": "GET",
        "variables": {
            "pagePagination": {
                "offset": 0,
                "limit": 10
            },
            "sectionPagination": {
                "offset": 0,
                "limit": 99
            }
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "864fdecccb9bb893141df3776d0207886c7fa781d9e586b9d4eb3afa387eea42"
            }
        }
    },
    "browsePage": {
        "method": "GET",
        "variables": {
            "pagePagination": {
                "offset": 0,
                "limit": 10
            },
            "sectionPagination": {
                "offset": 0,
                "limit": 10
            },
            "uri": "spotify:page:0JQ5DAqbMKFA6SOHvT3gck"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "ad382fb883bf67ab7af931edfc7ba4ffbc9a6e5a41ca59d1bafd8edd0c82bae1"
            }
        }
    },
    "browseSection": {
        "method": "GET",
        "variables": {
            "pagination": {
                "offset": 0,
                "limit": 20
            },
            "uri": "spotify:section:0JQ5IMCbQBLvmz1fA0GeCd"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "d453095dc74133219c80ee97c9c8291a0f56f27369a20d057039978ffded0762"
            }
        }
    },
    "fetchAlbumForRecentlyPlayed": {
        "method": "GET",
        "variables": {
            "uri": "spotify:album:0jmSaEG7ah3dpH8Sn2pDhp"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "4b210cde21b092f94056b108317be7ddc917e99cc684138ffceae32d8fb1a3f1"
            }
        }
    },
    "fetchTrackForRecentlyPlayed": {
        "method": "GET",
        "variables": {
            "uri": "spotify:track:5wNZQLv9dbaRI1u4yPMUTF"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "8e00e36a96b1a6a028437033c507e52d0c3b400537b0fa02f7e005856f31afed"
            }
        }
    },
    "decoratePlaylists": {
        "method": "GET",
        "variables": {
            "uris": [
                "spotify:playlist:0nPVftVdvERZwOTdvIMiem",
                "spotify:playlist:24tWr8zUVfG293RxnjQEAA",
                "spotify:playlist:4SASoCfBsMOCzVVIHRiaza",
                "spotify:playlist:7116NaHo5yygkAjoBmLaIq",
                "spotify:playlist:2FwLrfBgh1fyI5wfFc988b",
                "spotify:playlist:4O37Nstn92l8KVJhxme05s",
                "spotify:playlist:37i9dQZF1DWUxyGpMcGpaI",
                "spotify:playlist:7rKRG6MMRWbXbxdllpgVIV",
                "spotify:playlist:7kO4i2d6vWqdYOS3ArBLyt",
                "spotify:playlist:49PRRRX1CToIIf2aylWUYu",
                "spotify:playlist:6mMQrz117EzTf07FOW9cKc",
                "spotify:playlist:3YdZ1QOCvvZjXhmbjM9Kaz",
                "spotify:playlist:6e492c7mLPv2p7DPecgTlD",
                "spotify:playlist:1kNluw9lojM3XPxulTpjHE",
                "spotify:playlist:1eEUmT3H46Joq4gquc1Adu",
                "spotify:playlist:37i9dQZF1DXcNf6sH1qnKU",
                "spotify:playlist:37i9dQZF1EIcwtrihYBzLc",
                "spotify:playlist:2tqRhuVKwWaicoID8BkBdp",
                "spotify:playlist:65h8sQ12OAEjW2CLWLJpCl",
                "spotify:playlist:0Zarq4BVkFkZOWkmqsfrjA",
                "spotify:playlist:37i9dQZF1DWYXEO3u0YOMv",
                "spotify:playlist:37i9dQZF1DWXLeA8Omikj7",
                "spotify:playlist:37i9dQZF1DWZKQs3zP6ZD6",
                "spotify:playlist:37i9dQZF1DX2niMzbAczXW",
                "spotify:playlist:1UzbR8Y832k48Y643GZxKF",
                "spotify:playlist:37i9dQZF1DXbVhgADFy3im",
                "spotify:playlist:5kDER2USpWsUXn4f1exE5G",
                "spotify:playlist:0ZTjaygTtjV0IFiNKjFiYQ",
                "spotify:playlist:3u0siCyVjXkIUZlOuNWULW",
                "spotify:playlist:16o6Ci5CJ53UCEfYpExsVN",
                "spotify:playlist:0iAeUtwINlqfjwAyQ4ykur",
                "spotify:playlist:37i9dQZF1DX5bKKZsnMo7c",
                "spotify:playlist:37i9dQZF1EXyxgskQM20NG",
                "spotify:playlist:6qm90HE8zCyMxdzAtPi6Om",
                "spotify:playlist:3CvPLrOpi1OXca1jyeRhs2",
                "spotify:playlist:2TO1OzIrh0Vw0jmCDMMMwk",
                "spotify:playlist:37i9dQZF1E4zceF7KIymQo",
                "spotify:playlist:37i9dQZF1DX9v9O7wB8rQi",
                "spotify:playlist:0IQiYQCCQudCeIek7F899w",
                "spotify:playlist:5HWzGIqwxw5jULrkFDoncm",
                "spotify:playlist:37i9dQZF1DX1tyCD9QhIWF",
                "spotify:playlist:7k0HJHyA0kdw1UhWX9lmMX",
                "spotify:playlist:6qMjrTiZxNa724sjybhcQj",
                "spotify:playlist:5IXfJqksbGE2mulfH9pGUG",
                "spotify:playlist:1ddlJnKaqx0ASEFPylNAnP",
                "spotify:playlist:6E4LU6LXXYXXoCFGbgWAxH",
                "spotify:playlist:3Py5t0rpoAlc2noUH9ppRL",
                "spotify:playlist:58gBAz2CWuzbtVPwl83oMd",
                "spotify:playlist:3qxSuTNp8RQ3QAnsQkMan4",
                "spotify:playlist:4PeBeoOKbrQJMlY6w9epnH"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "bc11db3d3a456e7f2d75ee30c81d61ef6d8697716a57906344f02c15425eab3a"
            }
        }
    },
    "searchDesktop": {
        "method": "GET",
        "variables": {
            "searchTerm": "lmao",
            "offset": 0,
            "limit": 10,
            "numberOfTopResults": 5,
            "includeAudiobooks": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "1d3a8f81abf4f33f49d1e389ed0956761af669eedb62a050c6c7bce5c66070bb"
            }
        }
    },
    "addToLibrary": {
        "method": "POST",
        "variables": {
            "uris": [
                "spotify:track:4akqPnWyCOWL0QNxQsXsNk"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "656c491c3f65d9d08d259be6632f4ef1931540ebcf766488ed17f76bb9156d15"
            }
        }
    },
    "removeFromLibrary": {
        "method": "POST",
        "variables": {
            "uris": [
                "spotify:track:5K1EwbZ0vBR2YDKRhGtBy5"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "1103bfd4b9d80275950bff95ef6d41a02cec3357e8f7ecd8974528043739677c"
            }
        }
    },
    "fetchExtractedColors": {
        "method": "GET",
        "variables": {
            "uris": [
                "https://newjams-images.scdn.co/image/ab676477000033ad/dt/v3/discover-weekly/aAbca4VNfzWuUCQ_FGiEFA==/bmVuZW5lbmVuZW5lbmVuZQ=="
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "d7696dd106f3c84a1f3ca37225a1de292e66a2d5aced37a66632585eeb3bbbfa"
            }
        }
    },
    "homeSection": {
        "method": "GET",
        "variables": {
            "uri": "spotify:section:0JQ5DAqbMKFwJhEbnbBUE9",
            "timeZone": "Asia/Kolkata"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "60c1b102f74bea3bb2062eb4b3979860c7ff5c96f4e9586e9f8bfa8619c8ad07"
            }
        }
    },
    "searchTracks": {
        "method": "GET",
        "variables": {
            "searchTerm": "ello",
            "offset": 0,
            "limit": 100,
            "numberOfTopResults": 20,
            "includeAudiobooks": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "1d021289df50166c61630e02f002ec91182b518e56bcd681ac6b0640390c0245"
            }
        }
    },
    "searchFullEpisodes": {
        "method": "GET",
        "variables": {
            "searchTerm": "ello",
            "offset": 0,
            "limit": 30
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "fecae17eb7235aef0942d1fec25ea6d56de9506cfb8333f9a9afe3a62ff71537"
            }
        }
    },
    "areEpisodesInLibrary": {
        "method": "GET",
        "variables": {
            "uris": [
                "spotify:episode:546YTfNrS79rGH8e8r3jKm",
                "spotify:episode:1b2FxkLPnvmH0SrbLecf1q",
                "spotify:episode:18cKNuAaMWtrzRZayl75UL",
                "spotify:episode:0tYZHSTdTZBSoQDAJJl3tx",
                "spotify:episode:3zvDPKu9Y8dyoMIqWxvlGE",
                "spotify:episode:3ACVW8MxJy7xJO6iDb6ly6",
                "spotify:episode:0J3OtEnegISzVBek09Q4I2",
                "spotify:episode:06Cw1L5X4MuBKLpKQgHTxT",
                "spotify:episode:3ofY4z0IMuOKnFCnxAl6ka",
                "spotify:episode:4Fsx9jSZIEB267lywMRs9c",
                "spotify:episode:0fxUDjAUN1tcU4tFfy7sic",
                "spotify:episode:2wdU895wA8GVczmsJxSgQA",
                "spotify:episode:6QwrJejFz9P9TJLEwQBTg5",
                "spotify:episode:2PT4D6zPfHyMoLl7mj3wik",
                "spotify:episode:5UziZfAa6sQL0aE7nDA638",
                "spotify:episode:6NlUx1yhm2uZEopGWzbGm9",
                "spotify:episode:0S1lPd0x8t0wye3Ysidkm9",
                "spotify:episode:6xY2q2N3dnBRpMlIgeGTJf",
                "spotify:episode:2dbzTx8ERlSM0GfcY1foag",
                "spotify:episode:4EG5mL1DbgMVJ6Hrw1jai2",
                "spotify:episode:5ZkRKUsRHoEAa5vjCKkjfG",
                "spotify:episode:5aaLFp7yOyEPwW5b3WSomN",
                "spotify:episode:2K3tpYpEKvtrTtt6BATEIx",
                "spotify:episode:415FXUkMhmwpewbdrq9tte",
                "spotify:episode:08Tab7sPcGARoZix3QOgn6",
                "spotify:episode:5GGnfxwphnoUcmIyyR9iMB",
                "spotify:episode:4YxBeQSktf9CsRHIlyilHk",
                "spotify:episode:63pA4FG8BKjTrsls4GI1ZN",
                "spotify:episode:2Oqg3ghaN8flnH8jIG16YB",
                "spotify:episode:0PemcI7loyx6VrODVXPqqY"
            ]
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "898ca7d4bb3f943f8682c99cfcded0add82c8a099a8701a9f4f38ec5af9919c3"
            }
        }
    },
    "searchAlbums": {
        "method": "GET",
        "variables": {
            "searchTerm": "ello",
            "offset": 0,
            "limit": 30,
            "numberOfTopResults": 20,
            "includeAudiobooks": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "37197f541586fe988541bb1784390832f0bb27e541cfe57a1fc63db3598f4ffd"
            }
        }
    },
    "searchArtists": {
        "method": "GET",
        "variables": {
            "searchTerm": "ello",
            "offset": 0,
            "limit": 30,
            "numberOfTopResults": 20,
            "includeAudiobooks": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "4e7cdd33163874d9db5e08e6fabc51ac3a1c7f3588f4190fc04c5b863f6b82bd"
            }
        }
    },
    "searchUsers": {
        "method": "GET",
        "variables": {
            "searchTerm": "ello",
            "offset": 0,
            "limit": 30,
            "numberOfTopResults": 20,
            "includeAudiobooks": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "f82af76fbfa6f57a45e0f013efc0d4ae53f722932a85aca18d32557c637b06c8"
            }
        }
    },
    "searchPlaylists": {
        "method": "GET",
        "variables": {
            "searchTerm": "ello",
            "offset": 0,
            "limit": 30,
            "numberOfTopResults": 20,
            "includeAudiobooks": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "87b755d95fd29046c72b8c236dd2d7e5768cca596812551032240f36a29be704"
            }
        }
    },
    "getAlbumMetadata": {
        "method": "GET",
        "variables": {
            "uri": "spotify:album:6edaehdD31qd3pTwaGhSFT"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "40a04a8555b99c39ba71648c044e32363655d44d3253fd59b31ac1d027b38224"
            }
        }
    },
    "queryAlbumMerch": {
        "method": "GET",
        "variables": {
            "uri": "spotify:album:6edaehdD31qd3pTwaGhSFT"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "cfd5277f1b57095a2ad68f6665f1a4d623f1c1b671b8eecd7aa6d0be0d825fe2"
            }
        }
    },
    "queryAlbumTracks": {
        "method": "GET",
        "variables": {
            "uri": "spotify:album:6edaehdD31qd3pTwaGhSFT",
            "offset": 0,
            "limit": 300
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "f387592b8a1d259b833237a51ed9b23d7d8ac83da78c6f4be3e6a08edef83d5b"
            }
        }
    },
    "fetchLibraryShows": {
        "method": "GET",
        "variables": {
            "offset": 0,
            "limit": 1
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "5654e4687d58b67f1d1cc282042bd7b61df010d6c0d7fbefee3cb0ac1c5aa0fb"
            }
        }
    },
    "fetchLibraryArtists": {
        "method": "GET",
        "variables": {
            "offset": 0,
            "limit": 1
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "a6ccd8682575544ef615aa011d98a27310ae87c7003c2bf58965f1ed2bc8f31e"
            }
        }
    },
    "fetchLibraryAlbums": {
        "method": "GET",
        "variables": {
            "offset": 0,
            "limit": 1
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "e18c65b7c99cd9c92545c6aa7d463170760bed0123ac01d85caca1fc3ff2ab67"
            }
        }
    },
    "queryShowMetadataV2": {
        "method": "GET",
        "variables": {
            "uri": "spotify:show:2jyRVoDZxyNzilVdmq7U3B"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "71cb75b2c59fe50099e7f687b9c9cb5cbfb3f6eecd07740725ee818dec93d80e"
            }
        }
    },
    "queryPodcastEpisodes": {
        "method": "GET",
        "variables": {
            "uri": "spotify:show:2jyRVoDZxyNzilVdmq7U3B",
            "offset": 0,
            "limit": 50
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "a1039c4916b9a212042a976e37865a600d129c473f1e967d50ee56899f8cb44c"
            }
        }
    },
    "queryArtistOverview": {
        "method": "GET",
        "variables": {
            "uri": "spotify:artist:1QAJqy2dA3ihHBFIHRphZj"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "a59275671d030e756e5b181cd65660b283d726e2da23981b16b4242f375af385"
            }
        }
    },
    "getEpisodeOrChapter": {
        "method": "GET",
        "variables": {
            "uri": "spotify:episode:5lj0tvGafoEG33WkGCOypH"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "c6476eb4b39af5503875aa8c8302afa0145e2aa8ab535fb840e7067148ad0d50"
            }
        }
    }
}
