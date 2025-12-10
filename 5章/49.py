from transformers import AutoTokenizer

# 東北大BERTの日本語トークナイザを利用
tokenizer = AutoTokenizer.from_pretrained("cl-tohoku/bert-base-japanese")

text = """
吾輩は猫である。名前はまだ無い。
どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。
吾輩はここで始めて人間というものを見た。……
（レポート用にはここに全文を入れる）
"""

tokens = tokenizer.tokenize(text)
print("トークン数:", len(tokens))
print(tokens[:100])  # 多すぎるときは先頭だけ表示
