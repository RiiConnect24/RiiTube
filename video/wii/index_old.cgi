#!/usr/bin/env python3
from cgi import FieldStorage
from pytube import YouTube
from sys import stdout
import io
import requests
import subprocess

form = FieldStorage()

video_url = "https://youtube.com/watch?v=" + form["q"].value

try:
    if form["site"].value == "vimeo":
        video_url = "https://vimeo.com/" + form["q"].value
    elif form["site"].value == "dailymotion":
        video_url = "https://dailymotion.com/video/" + form["q"].value
except:
    pass

stdout.buffer.write(b"Content-Type:application/octet-stream\n\n")
stdout.flush()

if "youtube" in video_url:
    url = YouTube("https://www.youtube.com/watch?v=" + form["q"].value).streams.get_lowest_resolution().url

    r = requests.get(url, stream=True)

    for chunk in r.iter_content(chunk_size=2048):
        stdout.flush()
        stdout.buffer.write(chunk)

else:
    if "vimeo" in video_url:
        protocol = "https"

    elif "dailymotion" in video_url:
        protocol = "http"

    proc = subprocess.Popen(["yt-dlp", "-f", "[width<=640]", "-f", "[protocol=" + protocol + "]", video_url, "-o", "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    """for line in io.TextIOWrapper(proc.stderr, encoding="utf-8"):
        if "Invoking downloader" in line:
            url = line.replace("[debug] Invoking downloader on ", "")[1:-2]
            break"""

    for chunk in iter(proc.stdout):
        stdout.flush()
        stdout.buffer.write(chunk)
