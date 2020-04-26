![x](https://imgur.com/ggW0ElK.png)
## Dependencies
[python 3.x](https://www.python.org/downloads/)

[requests](https://requests.readthedocs.io/en/master/)

[notify-send](https://ss64.com/bash/notify-send.html) (should be natively installed on ubuntu)

leenux

## Usage
#### Adding streamers to track
`python3 main.py add [username]` e.g. asmongold, jerma985, etc
#### Removing tracked streamers
`python3 main.py remove [username]`
#### Listing tracked streamers
`python3 main.py list`
#### Running the main background process / alerting you of when someone goes live
`python3 main.py` (just call the file with no args)
