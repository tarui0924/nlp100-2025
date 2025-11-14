# 17.py 1列目の文字列の異なり（ユニークな名前の集合）

filename = "popular-names.txt"

names = set()

with open(filename, encoding="utf-8") as f:
    for line in f:
        cols = line.rstrip("\n").split("\t")
        if cols:
            names.add(cols[0])

for name in sorted(names):
    print(name)
