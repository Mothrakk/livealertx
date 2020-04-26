import requests
import os

from paths import Paths

from typing import Union, Dict

def client_id() -> str:
    return "vdl6udd3nelaw38jh2prltfvflb5rm" # this is ok to be public

def custom_headers() -> Dict[str, str]:
    return { "Client-ID": client_id() }

def fetch_pfp(name: str, url: str) -> None:
    os.makedirs(Paths.PFP, exist_ok=True)
    response = requests.get(url)
    with open(f"{Paths.PFP}/{name}.png", "wb") as fptr:
        fptr.write(response.content)

def username_exists(user: str) -> Union[None, bool]:
    response = requests.get(f"https://api.twitch.tv/helix/users?login={user}", headers=custom_headers())
    if response.status_code == 200:
        j = response.json()
        if j["data"] and j["data"][0]["display_name"] + ".png" not in os.listdir(Paths.PFP):
            fetch_pfp(j["data"][0]["display_name"], j["data"][0]["profile_image_url"])
        return bool(j["data"])
