#!/usr/bin/env python
import sys
import glob

target = sys.argv[1]

for idxfile in glob.glob(f"index/tel/{target}/*.dat"):
    index = open(idxfile).read().split(",")
    print(index)

    file = index[0]
    begin = int(index[1])
    len = int(index[2])

    with open(file) as f:
        f.seek(begin)
        print(f.read(len))
