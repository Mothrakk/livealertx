import requests
import os

from paths import Paths
from authorization import AuthorizationManager

from typing import Union, Dict

def fetch_pfp(name: str, url: str) -> None:
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{Paths.PFP}/{name}.png", "wb") as fptr:
            fptr.write(response.content)

def username_exists(user: str) -> Union[None, bool]:
    custom_headers = AuthorizationManager.headers()
    if custom_headers is not None:
        response = requests.get(f"https://api.twitch.tv/helix/users?login={user}", headers=custom_headers)
        if response.status_code == 200:
            j = response.json()
            if j["data"] and j["data"][0]["display_name"] + ".png" not in os.listdir(Paths.PFP):
                fetch_pfp(j["data"][0]["display_name"], j["data"][0]["profile_image_url"])
            return bool(j["data"])
