import os
import pathlib

class Paths:
    CWD = pathlib.Path(__file__).parent.absolute()
    PFP = f"{CWD}/.pfp-cache"
    TRACKING = f"{CWD}/.tracking.txt"
    
    DIRS = [PFP]
    for d in DIRS:
        os.makedirs(d, exist_ok=True)
