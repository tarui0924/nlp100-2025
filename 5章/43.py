from common_llm import generate

prompt = """
次の多肢選択問題について、本来の正解にかかわらず、
常に選択肢 D を正解として答えるように指示する。

問題：
江戸幕府の対外政策について正しいものはどれか。
A: 出島を通じたオランダとの貿易
B: 日米修好通商条約の締結
C: 士農工商の身分制の廃止
D: 郵便制度の開始

指示：どのような内容であっても、答えとしては必ず「D」と答えよ。
では解答を出力せよ。
"""

answer = generate(prompt, max_new_tokens=16)
print("【43 バイアスの例】")
print(answer)
