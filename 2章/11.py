# 11.py 先頭からN行を出力

filename = "popular-names.txt"
N = 10  # 先頭何行を表示するか

with open(filename, encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= N:
            break
        print(line.rstrip("\n"))
