# 23.py セクション名とレベルの表示

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

section_pattern = re.compile(r"^(=+)\s*(.+?)\s*\1$")

for line in text.split("\n"):
    m = section_pattern.match(line)
    if m:
        level = len(m.group(1)) - 1  # "="の数-1をレベルとする
        name = m.group(2)
        print(level, name)
