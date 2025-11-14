# 10.py 行数のカウント

filename = "popular-names.txt"

count = 0
with open(filename, encoding="utf-8") as f:
    for _ in f:
        count += 1

print(count)
