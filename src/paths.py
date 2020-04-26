import pathlib

class Paths:
    CWD = pathlib.Path(__file__).parent.absolute()
    PFP = f"{CWD}/.pfp-cache"
    TRACKING = f"{CWD}/.tracking.txt"
