import os.path

from paths import Paths

from typing import Set

class Tracking:
    @staticmethod
    def get() -> Set:
        tracking = set()
        if os.path.exists(Paths.TRACKING):
            with open(Paths.TRACKING) as fptr:
                tracking = set(fptr.read().strip().split("\n"))
        return tracking

    @staticmethod
    def set(contents: Set) -> None:
        with open(Paths.TRACKING, "w") as fptr:
            fptr.write("\n".join(contents))
