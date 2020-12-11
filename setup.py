#!/usr/bin/env python3
from setuptools import setup

setup(name="partial-twitch-downloader",
      version="1.0.0",
      description="Make a partial download of a Twitch VOD using by downloading only some segments and combining them.",
      url="https://github.com/Rayquaza01/partial-twitch-downloader",
      license="MIT",
      scripts=["bin/partial-twitch-downloader.py"],
      install_requires=["youtube-dl", "ffmpeg-python"],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ])
