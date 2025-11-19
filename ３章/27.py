# 27.py 基礎情報から内部リンク [[...]] を除去

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

def extract_basic_info(text: str) -> dict:
    m = re.search(r"^\{\{基礎情報.*?\n(.*?)\n\}\}$",
                  text, flags=re.MULTILINE | re.DOTALL)
    if not m:
        return {}
    body = m.group(1)
    info = {}
    current_key = None
    for line in body.split("\n"):
        if line.startswith("|"):
            key, value = re.split(r"\s*=\s*", line[1:], 1)
            info[key] = value
            current_key = key
        else:
            if current_key:
                info[current_key] += "\n" + line
    return info

def remove_markup(text: str) -> str:
    # 強調
    text = re.sub(r"'{2,5}", "", text)
    # 内部リンク [[記事名|表示名]] / [[記事名]]
    text = re.sub(r"\[\[([^|\]]*\|)?([^|\]]+)\]\]", r"\2", text)
    return text

text = get_uk_text()
basic = extract_basic_info(text)

for k, v in basic.items():
    basic[k] = remove_markup(v)

for k, v in basic.items():
    print(f"{k}: {v}")
