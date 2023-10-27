#!/usr/bin/env python3
from cgi import FieldStorage
import vimeo

v = vimeo.VimeoClient(
    token="b0acb6b53986ddef2c2cb4417c627bce",
    key="57495f1cd3af69fc968bbf6df62eebc9fe4a3063",
    secret="NCCiDI8jX8h8sXX21drIl/00AGXKCUKO6il8mOqyZvgV7bvsgs4fTLzeSqPt0u+BoIns1ZDV6V2KtzPffyGTjS6DpepE5g/RBcAKKsDChnPyErNrpcT9FbfFnB1i6Jk9"
)

form = FieldStorage()

api = v.get('/videos', params={"query": form["q"].value, "per_page": 50}).json()["data"]

print("Content-Type: text/plain;charset=UTF-8;\n");

print("[Playlist]")

for i, entry in enumerate(api, start=1):
    print(
        f"File{str(i)}=http://riitube.rc24.xyz/video/wii/?q="
        + entry["link"].replace("https://vimeo.com/", "")
        + "&site=vimeo"
    )
    print(f"Title{str(i)}=" + entry["name"])
    print(f"Length{str(i)}=" + str(entry["duration"]))
