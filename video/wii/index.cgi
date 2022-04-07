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

if "youtube" in video_url or "vimeo" in video_url:
    proc = subprocess.Popen(["yt-dlp", "-f", "[width<=640]", video_url, "-o", "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

elif "dailymotion" in video_url:
    proc = subprocess.Popen(["yt-dlp", "-f", "[tbr<=850]", video_url, "-o", "-"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for chunk in iter(proc.stdout):
    stdout.flush()
    stdout.buffer.write(chunk)
