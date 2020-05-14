#!/usr/bin/env python3

import os
import time
import sys
import requests

from paths import Paths
from tracking import Tracking
from utils import custom_headers
from argparsing import Parser

def notify(name: str, title: str) -> None:
    query = ("notify-send",
            f'-i "{Paths.PFP}/{name}.png"',
            f'"{name} is live!"',
            f'"{title}"')
    os.system(" ".join(query))
    
def loop(TICK_RATE_SECONDS: int) -> None:
    previously_live = set()

    while True:
        tracking = Tracking.get()
        if tracking:
            query = f"https://api.twitch.tv/helix/streams?{'&'.join((f'user_login={x}' for x in tracking))}"
            response = requests.get(query, headers=custom_headers())
            if response.status_code == 200:
                j = response.json()
                if j["data"]:
                    live_now = {
                        dp["user_name"] : {"title": dp["title"]}
                        for dp in j["data"]
                    }
                    for k in set(live_now).difference(previously_live):
                        notify(k, live_now[k]["title"])
                    previously_live = set(live_now)

        time.sleep(TICK_RATE_SECONDS)

if len(sys.argv) < 2:
    loop(10)
else:
    if sys.argv[1] in Parser.options:
        Parser.options[sys.argv[1]]()
    else:
        print(f"options: {'|'.join(Parser.options)}")
