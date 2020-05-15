import sys
import os

from paths import Paths
from utils import username_exists
from tracking import Tracking
from authorization import AuthorizationManager

from typing import Union, Dict

argc = len(sys.argv)

class Parser:
    @staticmethod
    def lst() -> None:
        r = Tracking.get()
        if r:
            print(", ".join(r))
        else:
            print(f"{Paths.TRACKING} is empty")

    @staticmethod
    def add() -> None:
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

    @staticmethod
    def remove() -> None:
        if argc < 3:
            print("missing arg: remove (username)")
        else:
            r = Tracking.get()
            if sys.argv[2] in r:
                r.remove(sys.argv[2])
                Tracking.set(r)
                for f in os.listdir(Paths.PFP):
                    if f.split(".")[0].lower() == sys.argv[2].lower():
                        os.remove(f"{Paths.PFP}/{f}")
                        break
            else:
                print(f"{sys.argv[2]} not being tracked")

Parser.options = {
    "list": Parser.lst,
    "add": Parser.add,
    "remove": Parser.remove
}
