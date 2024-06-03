#!/usr/bin/python
import os
import sys
import shutil
from urllib.parse import quote

directory = sys.argv[1]
prefix = sys.argv[2] if sys.argv[2] != "local" else ""
thumb_prefix = sys.argv[3] if sys.argv[3] != "local" else ""
ignore_files = sys.argv[4].split(",") if sys.argv[4] != "none" else ""
content = ""

with open("template.html", "r") as f:
    template = f.read()

files = os.listdir(directory)
files.sort(key=lambda x: os.path.getmtime(f"{directory}/{x}"))
for file in reversed(files):
    if file in ignore_files:
        continue
    content += f"<a href=\"{prefix}{quote(file)}\">"
    if file.endswith(".mp4"):
        file_gif = file.replace(".mp4", ".gif")
        content += f"<img loading=\"lazy\" class=\"thumbnail\" src=\"{thumb_prefix}thumbs/{quote(file_gif)}\">"
    elif file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        file_jpg = file.replace(".png", ".jpg").replace(".jpeg", ".jpg")
        content += f"<img loading=\"lazy\" class=\"thumbnail\" src=\"{thumb_prefix}thumbs/{quote(file_jpg)}\">"
    content += "</a>"

with open("index.html", "w") as f:
    f.write(template.replace("{content}", content))
