# 14.py 1列目を出力

filename = "popular-names.txt"

with open(filename, encoding="utf-8") as f:
    for line in f:
        cols = line.rstrip("\n").split("\t")
        if cols:
            print(cols[0])
