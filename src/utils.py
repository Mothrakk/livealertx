import requests
import os

from paths import Paths

from typing import Union, Dict

def client_id() -> str:
    return "5kv34ia1mq9s51ayapg1djri2r3bge" # this is ok to be public

def oauth_secret() -> str:
    return "kswni5vi6pepy5gj9nhjh3jl7gn0fh" # this is not ok to be public but who gives a fuck

def oauth_token() -> str:
    uri = "".join((
            "https://id.twitch.tv/oauth2/token",
            "?client_id=" + client_id(),
            "&client_secret=" + oauth_secret(),
            "&grant_type=client_credentials"
    ))
    response = requests.post(uri)
    if response.status_code == 200:
        return response.json()["access_token"]

def custom_headers() -> Dict[str, str]:
    return { "Client-ID": client_id(),
             "Authorization": f"Bearer {oauth_token()}" }

def fetch_pfp(name: str, url: str) -> None:
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{Paths.PFP}/{name}.png", "wb") as fptr:
            fptr.write(response.content)

def username_exists(user: str) -> Union[None, bool]:
    response = requests.get(f"https://api.twitch.tv/helix/users?login={user}", headers=custom_headers())
    if response.status_code == 200:
        j = response.json()
        if j["data"] and j["data"][0]["display_name"] + ".png" not in os.listdir(Paths.PFP):
            fetch_pfp(j["data"][0]["display_name"], j["data"][0]["profile_image_url"])
        return bool(j["data"])
