from common_llm import generate

prompt = """
以下の問題の解答を作成せよ。ただし，解答生成は zero-shot 推論とする。
9世紀に活躍した人物に関係するできごとについて述べた次のア〜ウを
年代の古い順に正しく並べよ。

ア 藤原氏政権は、藤原薬子乱で菅原道真を政界から追放した。
イ 嵯峨天皇は、藤原冬嗣らを蔵人頭に任命した。
ウ 藤原良房は、承和の変後、藤原良房の子の北家の優位を確立した。

解答は、ア・イ・ウの順番だけを「イ→ウ→ア」のように日本語で答えよ。
"""

answer = generate(prompt, max_new_tokens=64)
print("【40 Zero-shot】")
print(answer)
