from common_llm import generate

conversation = """
ユーザ: 自由が丘で急行に乗り間違えたときの目的地の駅名は何ですか？
システム: （ここに先ほどの回答があると仮定する）

ユーザ: では、今度は自由が丘で反対方向の急行に乗り間違えたとする。
目的地にはどのように向かえばよいか、何駅で降りればよいかを説明せよ。
システム:
"""

answer = generate(conversation, max_new_tokens=96)
print("【45 マルチターン対話】")
print(answer)
