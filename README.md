![x](https://imgur.com/ggW0ElK.png)
## Dependencies
[python 3.x](https://www.python.org/downloads/)

[requests](https://requests.readthedocs.io/en/master/) (`python3 -m pip install requests`)

[notify-send](https://ss64.com/bash/notify-send.html) (should be natively installed on ubuntu)

leenux

## Usage
#### Adding streamers to track
`python3 livealertx.py add [username]` e.g. asmongold, jerma985, etc
#### Removing tracked streamers
`python3 livealertx.py remove [username]`
#### Listing tracked streamers
`python3 livealertx.py list`
#### Running the main background process / alerting you of when someone goes live
`python3 livealertx.py` (just call the file with no args)
#### Running the script on startup
Give `livealertx.py` executive privileges with `chmod +x livealertx.py` and then follow your distro's guide to launching executables on startup. On Ubuntu it's straightforward:

![y](https://imgur.com/19GXS9N.png)