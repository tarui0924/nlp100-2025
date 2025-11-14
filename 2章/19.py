# 19.py 3列目の数値の降順で各行を並び替え

filename = "popular-names.txt"

with open(filename, encoding="utf-8") as f:
    rows = [line.rstrip("\n").split("\t") for line in f]

# 3列目 (index 2) を整数として解釈し、降順にソート
rows.sort(key=lambda row: int(row[2]), reverse=True)

for row in rows:
    print("\t".join(row))
