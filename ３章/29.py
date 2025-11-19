# 29.py 国旗画像のURLを取得

import json
import gzip
import re
import requests  # 事前に `pip install requests` しておく

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

text = get_uk_text()
basic = extract_basic_info(text)

flag_file = basic.get("国旗画像")
if not flag_file:
    raise SystemExit("国旗画像の項目が見つかりません")

# MediaWiki API を呼び出して画像URLを取得
url = "https://commons.wikimedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "titles": f"File:{flag_file}",
    "prop": "imageinfo",
    "iiprop": "url",
}

res = requests.get(url, params=params)
data = res.json()

pages = data["query"]["pages"]
page = next(iter(pages.values()))
image_url = page["imageinfo"][0]["url"]

print(image_url)
