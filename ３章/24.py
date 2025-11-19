# 24.py ファイル参照（メディアファイル名）の抽出

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

file_pattern = re.compile(r"\[\[(?:File|ファイル):(.+?)(?:\|.*)?\]\]")

for line in text.split("\n"):
    m = file_pattern.search(line)
    if m:
        print(m.group(1))
