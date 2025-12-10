from common_llm import generate

prompt = """
次の川柳の「面白さ」を、1〜10の整数で評価せよ。
最後に「スコア: X」の形式で数値だけを示すこと。

お題：学校
川柳：眠いけど　授業は進む　時計だけ遅い
"""

answer = generate(prompt, max_new_tokens=64)
print("【47 評価】")
print(answer)
