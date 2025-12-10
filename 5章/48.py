from common_llm import generate

prompt = """
次の川柳の面白さを、1〜10の整数で評価せよ。
最後に「スコア: X」の形式で数値を示すこと。

川柳：昼休み　屋上風が　気持ちいい
"""

print("【48 評価のぶれ】")
for i in range(5):
    answer = generate(prompt, max_new_tokens=64)
    print(f"{i+1}回目:", answer)
