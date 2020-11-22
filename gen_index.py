#!/usr/bin/env python
import os
import glob

for file in glob.glob("data/*.csv")[:1]:
    lines = open(file).readlines()
    i = 0
    for line in lines:
        begin = i
        llen = len(line)

        data = line.split(",")
        uuid = data[1]
        tel = data[2]

        index = f"{file},{begin},{llen}"

        os.makedirs(f"index/tel/{tel}")
        with open(f"index/tel/{tel}/{uuid}.dat", "w") as f:
            f.write(f"{file},{begin},{llen}")

        i += llen

