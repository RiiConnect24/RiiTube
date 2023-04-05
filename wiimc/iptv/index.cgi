#!/usr/bin/env python3
from sys import stdout
from cgi import FieldStorage
from pytube import YouTube
import m3u8
import requests
import json
import urllib.parse

form = FieldStorage()

api = requests.get("https://iptv-org.github.io/iptv/index.m3u").content

print("Content-Type: text/plain;charset=UTF-8;\n");

print("[Playlist]")

i = 1

playlist = {}

last = ""

for entry in api.split(b"\n"):
    if b"#EXTINF" in entry and form["q"].value.encode().lower().replace(b" ", b"") in entry.split(b",")[-1].lower().replace(b" ", b""):
        last = entry.split(b",")[-1]
    elif last != "":
        if last not in playlist:
            playlist[last] = entry

i = 1

for entry in playlist:
    print("File" + str(i) + "=" + "http://riitube.rc24.xyz/video/wii/?q=" + urllib.parse.quote(playlist[entry]) + "&site=iptv")
    print("Title" + str(i) + "=" + entry.decode())
    print("Length" + str(i) + "=" + "9999999")

    i += 1
    # except:
        # continue
