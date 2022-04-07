#!/usr/bin/env python3
from cgi import FieldStorage
import vimeo

v = vimeo.VimeoClient(
    token="redacted",
    key="redacted",
    secret="redacted"
)

form = FieldStorage()

api = v.get('/videos', params={"query": form["q"].value, "per_page": 50}).json()["data"]

print("Content-Type: text/plain;charset=UTF-8;\n");

print("[Playlist]")

i = 1

for entry in api:
    print("File" + str(i) + "=" + "http://riitube.rc24.xyz/video/wii/?q=" + entry["link"].replace("https://vimeo.com/", "") + "&site=vimeo")
    print("Title" + str(i) + "=" + entry["name"])
    print("Length" + str(i) + "=" + str(entry["duration"]))

    i += 1
