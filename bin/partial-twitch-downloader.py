#!/usr/bin/env python3
import argparse
import urllib.request
import os
import youtube_dl
import ffmpeg

ap = argparse.ArgumentParser()
ap.add_argument("twitch_url", nargs=1, help="The location of the Twitch VOD")
args = vars(ap.parse_args())

with youtube_dl.YoutubeDL({}) as ytdl:
    ytdl_info = ytdl.extract_info(args["twitch_url"][0], download=False)

# get playlist location
playlist = ytdl_info["url"]
# get base url for ts files
base_url = "/".join(ytdl_info["url"].split("/")[:-1])
# get stream title
title = ytdl_info["title"]

# get playlist from web, determine maximum number of segments
# gets second to last line, which contains the last segment number
max_segments = int(urllib.request.urlopen(playlist)
                   .read().decode("utf-8")
                   .splitlines()[-2]
                   .split(".")[0])

print("{} has {} segments".format(title, max_segments))

# get segments to download from user
start = int(input("Enter start segment (0 to {}): ".format(max_segments)))
end = int(input("Enter end segment ({} to {}): ".format(start, max_segments)))

# if combined file already exists, remove it
if (os.path.isfile("combined.ts")):
    os.remove("combined.ts")

# open combined file in append bytes mode
with open("combined.ts", "ab") as f:
    for i in range(start, end + 1):
        # download segment
        segment = urllib.request.urlopen(base_url + "/" + str(i) + ".ts").read()
        # append to file
        f.write(segment)
        print("Segment {} written, {} bytes".format(i, len(segment)))

print("Converting to mp4")
stream = ffmpeg.input("combined.ts")
stream = ffmpeg.output(stream, "{}-{}-{}.mp4".format(title, start, end), **{
    "acodec": "copy",
    "vcodec": "copy"
})
ffmpeg.run(stream)

os.remove("combined.ts")
print("Done")
