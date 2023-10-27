#!/usr/bin/env python3
from cgi import FieldStorage
import dailymotion

form = FieldStorage()

d = dailymotion.Dailymotion()

api = d.get('/videos', params={"search": form["q"].value, "limit": 50})["list"]

print("Content-Type: text/plain;charset=UTF-8;\n");

print("[Playlist]")

for i, entry in enumerate(api, start=1):
    print(
        f"File{str(i)}=http://riitube.rc24.xyz/video/wii/?q="
        + entry["id"]
        + "&site=dailymotion".replace("https://dailymotion.com/", "")
    )
    print(f"Title{str(i)}=" + entry["title"])
    print(f"Length{str(i)}=0")
