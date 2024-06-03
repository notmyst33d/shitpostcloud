#!/usr/bin/python
import os
import sys
import shutil

directory = sys.argv[1]
output = sys.argv[2]
clean = sys.argv[3]

def thumb_video(file):
    file_gif = file.replace(".mp4", ".gif")
    if os.path.isfile(f"{output}/{file_gif}"):
        return
    print(f"Generating thumbnail for {file}")
    for i in range(5):
        os.system(f"ffmpeg -hide_banner -loglevel warning -y -i \"{directory}/{file}\" -ss 00:00:0{i}.000 -vframes 1 -update true /tmp/frame{i}.png")

    os.system("ffmpeg -hide_banner -loglevel warning -y -r 2 -i /tmp/frame%01d.png -vf scale=128:128 /tmp/thumb.gif")
    os.system("rm /tmp/frame*.png")
    shutil.move("/tmp/thumb.gif", f"{output}/{file_gif}")

def thumb_photo(file):
    file_jpg = file.replace(".png", ".jpg").replace(".jpeg", ".jpg")
    if os.path.isfile(f"{output}/{file_jpg}"):
        return
    print(f"Generating thumbnail for {file}")
    os.system(f"ffmpeg -hide_banner -loglevel warning -y -i \"{directory}/{file}\" -vf scale=128:128 -vframes 1 -update true \"{output}/{file_jpg}\"")

def clean_video(file):
    file_mp4 = file.replace(".gif", ".mp4")
    if not os.path.isfile(f"{directory}/{file_mp4}"):
        print(f"Delete {file}")
        os.remove(f"{output}/{file}")

def clean_photo(file):
    file_png = file.replace(".jpg", ".png")
    file_jpeg = file.replace(".jpg", ".jpeg")
    if not (os.path.isfile(f"{directory}/{file}") or os.path.isfile(f"{directory}/{file_png}") or os.path.isfile(f"{directory}/{file_jpeg}")):
        print(f"Delete {file}")
        os.remove(f"{output}/{file}")

for file in os.listdir(directory):
    if file.endswith(".mp4"):
        thumb_video(file)
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        thumb_photo(file)

if clean == "true":
    for file in os.listdir(output):
        if file.endswith(".gif"):
            clean_video(file)
        if file.endswith(".jpg"):
            clean_photo(file)
