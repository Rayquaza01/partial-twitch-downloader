# Partial Twitch Downloader

Make a partial download of a Twitch VOD using by downloading only some segments and combining them.

# Installation

Uses youtube-dl and ffmpeg-python

To install this program, use:
```
pip3 install git+https://github.com/Rayquaza01/partial-twitch-downloader
```

# Usage

```
usage: partial-twitch-downloader.py [-h] twitch_url

positional arguments:
  twitch_url  The location of the Twitch VOD

optional arguments:
  -h, --help  show this help message and exit
```

The script will tell you how many segments the VOD has, and will ask for the start segment and the end segment. It will save the VOD in the file `STREAM_TITLE-START-END.mp4`
