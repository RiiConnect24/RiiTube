#!/usr/bin/env python3
from sys import stdout
from cgi import FieldStorage
from pytube import YouTube
import requests
import json

form = FieldStorage()

if "q" in form.keys():
    api = requests.get("https://y.com.sb/api/v1/search?q=" + form["q"].value).json()
elif "trending" in form.keys():
    api = requests.get("https://y.com.sb/api/v1/trending").json()
else:
    api = requests.get("https://y.com.sb/api/v1/popular").json()

print("Content-Type: text/plain;charset=UTF-8;\n");

print("[Playlist]")

i = 1

for entry in api:
    print("File" + str(i) + "=" + "http://riitube.rc24.xyz/video/wii/?q=" + entry["videoId"])
    print("Title" + str(i) + "=" + entry["title"])
    print("Length" + str(i) + "=" + str(entry["lengthSeconds"]))

    i += 1
