#!/usr/bin/env python3
from sys import stdout
from cgi import FieldStorage
from pytube import YouTube
import requests
import json

form = FieldStorage()

url = YouTube("https://www.youtube.com/watch?v=" + form["q"].value).streams.get_lowest_resolution().url

stdout.buffer.write(b"Content-Type:application/octet-stream\n\n")
stdout.flush()

r = requests.get(url, stream=True)

for chunk in r.iter_content(chunk_size=2048):
    stdout.flush()
    stdout.buffer.write(chunk)
