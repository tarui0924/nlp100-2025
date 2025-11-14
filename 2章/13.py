# 13.py タブをスペースに置換

filename = "popular-names.txt"

with open(filename, encoding="utf-8") as f:
    for line in f:
        print(line.replace("\t", " "), end="")
