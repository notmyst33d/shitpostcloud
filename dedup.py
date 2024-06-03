#!/usr/bin/python
import os
import sys
import hashlib

target = sys.argv[1]

hashes = []

def md5file(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()

for file in os.listdir(target):
    if not os.path.isfile(f"{target}/{file}"):
        continue
    h = md5file(f"{target}/{file}")
    present = False
    for h2 in hashes:
        if h2[0] == h:
            print(f"Delete {file} (same as {h2[1]})")
            present = True
            #os.remove(f"{target}/{file}")
            break
    hashes.append((h, file))
