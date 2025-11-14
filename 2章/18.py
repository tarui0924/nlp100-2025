# 18.py 1列目の文字列の出現頻度を求め、多い順に並べる

from collections import Counter

filename = "popular-names.txt"

counter = Counter()

with open(filename, encoding="utf-8") as f:
    for line in f:
        cols = line.rstrip("\n").split("\t")
        if cols:
            counter[cols[0]] += 1

for name, freq in counter.most_common():
    print(name, freq)
