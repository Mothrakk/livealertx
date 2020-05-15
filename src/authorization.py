import requests
from time import time

from typing import Union, Dict

class TokenManager:
    def __init__(self, client_id: str, oauth_secret: str):
        self.client_id = client_id
        self.oauth_secret = oauth_secret
        self.new()

    def new(self) -> None:
        url = "".join((
                "https://id.twitch.tv/oauth2/token",
                "?client_id=" + self.client_id,
                "&client_secret=" + self.oauth_secret,
                "&grant_type=client_credentials"
        ))
        response = requests.post(url)
        if response.status_code == 200:
            j = response.json()
            self.token = j["access_token"]
            self.expires_in = j["expires_in"]
            self.acquired_at = time()
        else:
            self.token = None

    def is_valid(self) -> bool:
        return self.token is not None and (time() - self.acquired_at) < self.expires_in

class AuthorizationManager:
    CLIENT_ID = "5kv34ia1mq9s51ayapg1djri2r3bge" # this is ok to be public
    OAUTH_SECRET = "kswni5vi6pepy5gj9nhjh3jl7gn0fh" # this is not ok to be public but who gives a fuck
    token_manager = TokenManager(CLIENT_ID, OAUTH_SECRET)

    @staticmethod
    def headers(*, auto_fix = True) -> Union[None, Dict[str, str]]:
        if auto_fix and not AuthorizationManager.token_manager.is_valid():
            AuthorizationManager.token_manager.new()
        if AuthorizationManager.token_manager.is_valid():
            return {
                "Client-ID": AuthorizationManager.CLIENT_ID,
                "Authorization": f"Bearer {AuthorizationManager.token_manager.token}"
            }
