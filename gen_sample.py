#!/usr/bin/env python
import sys
import uuid
import string
import random
import multiprocessing

files = int(sys.argv[1])
rows = int(sys.argv[2])

def gen_row(rno):
    id = uuid.uuid4()
    tel = random.randint(10000000000, 99999999999)
    data = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    return f"{rno},{id},{tel},{data}"

def gen_file(fno):
    with open(f"data/{fno}.csv", "w") as f:
        for rno in range(rows):
            print(f"{fno}:{rno}")
            f.write(gen_row(rno))
            f.write("\n")

if __name__ == "__main__":
    p = multiprocessing.Pool(10)
    p.map(gen_file, range(files))
