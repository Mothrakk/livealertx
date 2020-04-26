![x](https://imgur.com/ggW0ElK.png)
## Dependencies
[python 3.x](https://www.python.org/downloads/)

[requests](https://requests.readthedocs.io/en/master/) (`python3 -m pip install requests`)

[notify-send](https://ss64.com/bash/notify-send.html) (should be natively installed on ubuntu) (`sudo apt-get install libnotify-bin`)

leenux

## Usage
#### Adding streamers to track
`python3 livealertx.py add [username]` e.g. asmongold, jerma985, etc
#### Removing tracked streamers
`python3 livealertx.py remove [username]`
#### Listing tracked streamers
`python3 livealertx.py list`
#### Running the main background process / alerting you of when someone goes live
<<<<<<< HEAD
`python3 livealertx.py` (just call the file with no args)
#### Running the script on startup
Give `livealertx.py` executive privileges with `chmod +x livealertx.py` and then follow your distro's guide to launching executables on startup. On Ubuntu it's straightforward:

![y](https://imgur.com/19GXS9N.png)
=======
`python3 main.py` (just call the file with no args)
#### Running the script on startup
Give `main.py` executive privileges with `chmod +x main.py`, then follow your distro's instructions to running something on boot. On Ubuntu it's pretty straightforward:
![y](https://imgur.com/xP9Wm40.png)
>>>>>>> ef22071241248e8003def5cb16fa271531413db2
