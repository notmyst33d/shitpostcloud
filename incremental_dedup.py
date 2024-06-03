#!/usr/bin/python
import os
import sys
import hashlib

reference = sys.argv[1]
target = sys.argv[2]

reference_hashes = []

def md5file(path):
    return hashlib.md5(open(path, "rb").read()).hexdigest()

for file in os.listdir(reference):
    if not file.endswith(".mp4"):
        continue

    reference_hashes.append(md5file(f"{reference}/{file}"))

for file in os.listdir(target):
    if md5file(f"{target}/{file}") in reference_hashes:
        print(f"Delete {file}")
        os.remove(f"{target}/{file}")
