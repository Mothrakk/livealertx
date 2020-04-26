import requests
import time
import os.path
import os
import sys
import pathlib

from typing import Set, Dict

CWD = pathlib.Path(__file__).parent.absolute()
PATH_PFP = f"{CWD}/.pfp-cache"
PATH_TRACKING = f"{CWD}/.tracking.txt"
os.makedirs(PATH_PFP, exist_ok=True)

H = { "Client-ID": "vdl6udd3nelaw38jh2prltfvflb5rm" } # this is ok to be public
TICK_RATE_SECONDS = 10

def fetch_pfp(name: str, url: str) -> None:
    response = requests.get(url)
    with open(f"{PATH_PFP}/{name}.png", "wb") as fptr:
        fptr.write(response.content)

def username_exists(user: str) -> bool:
    response = requests.get(f"https://api.twitch.tv/helix/users?login={user}", headers=H)
    if response.status_code == 200:
        j = response.json()
        if j["data"] and j["data"][0]["profile_image_url"] + ".png" not in os.listdir(PATH_PFP):
            fetch_pfp(j["data"][0]["display_name"], j["data"][0]["profile_image_url"])
        return bool(j["data"])

class Tracking:
    @staticmethod
    def get() -> Set:
        tracking = set()
        if os.path.exists(PATH_TRACKING):
            with open(PATH_TRACKING) as fptr:
                tracking = set(fptr.read().strip().split("\n"))
        return tracking

    @staticmethod
    def set(contents: Set) -> None:
        with open(PATH_TRACKING, "w") as fptr:
            fptr.write("\n".join(contents))

class Main:
    @staticmethod
    def notify(name: str, title: str) -> None:
        query = ("notify-send",
                f'-i "{PATH_PFP}/{name}.png"',
                f'"{name} is live!"',
                f'"{title}"')
        os.system(" ".join(query))
    
    @staticmethod
    def loop() -> None:
        previously_live = set()

        while True:
            tracking = Tracking.get()
            if tracking:
                query = f"https://api.twitch.tv/helix/streams?{'&'.join((f'user_login={x}' for x in tracking))}"
                response = requests.get(query, headers=H)
                if response.status_code == 200:
                    j = response.json()
                    if j["data"]:
                        live_now = {
                            dp["user_name"] : {"title": dp["title"]}
                            for dp in j["data"]
                        }
                        for k in set(live_now).difference(previously_live):
                            Main.notify(k, live_now[k]["title"])
                        previously_live = set(live_now)

            time.sleep(TICK_RATE_SECONDS)

argc = len(sys.argv)
if argc < 2:
    Main.loop()
else:
    OPTIONS = ("list", "add", "remove")
    if sys.argv[1] in OPTIONS:
        if sys.argv[1] == "list":
            r = Tracking.get()
            if r:
                print(", ".join(r))
            else:
                print(f"{PATH_TRACKING} is empty")
        elif sys.argv[1] == "add":
            if argc < 3:
                print("missing arg: add (username)")
            else:
                r = username_exists(sys.argv[2])
                if r is None:
                    print("Twitch API down, try again later")
                elif r:
                    r = Tracking.get()
                    r.add(sys.argv[2])
                    Tracking.set(r)
                else:
                    print(f"{sys.argv[2]} is not a valid Twitch username")
        elif sys.argv[1] == "remove":
            if argc < 3:
                print("missing arg: remove (username)")
            else:
                r = Tracking.get()
                if sys.argv[2] in r:
                    r.remove(sys.argv[2])
                    Tracking.set(r)
                else:
                    print(f"{sys.argv[2]} not being tracked")
    else:
        print(f"options: {'|'.join(OPTIONS)}")
