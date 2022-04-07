#!/usr/bin/env python3
from cgi import FieldStorage
import dailymotion

form = FieldStorage()

d = dailymotion.Dailymotion()

api = d.get('/videos', params={"search": form["q"].value, "limit": 50})["list"]

print("Content-Type: text/plain;charset=UTF-8;\n");

print("[Playlist]")

i = 1

for entry in api:
    print("File" + str(i) + "=" + "http://riitube.rc24.xyz/video/wii/?q=" + entry["id"] + "&site=dailymotion".replace("https://dailymotion.com/", ""))
    print("Title" + str(i) + "=" + entry["title"])
    print("Length" + str(i) + "=" + str(0))

    i += 1
