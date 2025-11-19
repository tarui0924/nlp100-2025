# 21.py カテゴリ名を含む行の抽出

import json
import gzip

def get_uk_text(filename="jawiki-country.json.gz"):
    with gzip.open(filename, "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            if article["title"] == "イギリス":
                return article["text"]
    return None

text = get_uk_text()

for line in text.split("\n"):
    if "[[Category:" in line:
        print(line)
