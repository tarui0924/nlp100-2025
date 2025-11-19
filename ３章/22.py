# 22.py カテゴリ名だけを抽出

import json
import gzip
import re

def get_uk_text(filename="jawiki-country.json.gz"):
    with gzip.open(filename, "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            if article["title"] == "イギリス":
                return article["text"]
    return None

text = get_uk_text()

pattern = re.compile(r"\[\[Category:(.*?)(?:\|.*)?\]\]")

for line in text.split("\n"):
    m = pattern.search(line)
    if m:
        print(m.group(1))
