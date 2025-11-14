# 12.py 末尾N行を出力

from collections import deque

filename = "popular-names.txt"
N = 10  # 末尾何行を表示するか

with open(filename, encoding="utf-8") as f:
    last_lines = deque(f, maxlen=N)

for line in last_lines:
    print(line.rstrip("\n"))
