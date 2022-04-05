# RiiTube
A way to watch YouTube on your Wii with WiiMC.

The code is extremely simple. All it does is:

1. Use Inviduous API to search for videos, or browse trending or popular videos (probably tech-related because that's what Inviduous tends to grab).
2. Returns a playlist file in WiiMC format.
3. Uses the pytube Python module to determine the exact URL of the video file, and proxies that to the Wii.

It's very simple, and I haven't seen any stuttering of the video or anything like that.