# 16.py ランダムに各行を並び替え

import random

filename = "popular-names.txt"

with open(filename, encoding="utf-8") as f:
    lines = f.readlines()

random.shuffle(lines)

for line in lines:
    print(line.rstrip("\n"))
