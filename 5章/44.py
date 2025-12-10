from common_llm import generate

prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えた。
東急大井町線の大井町方面の電車に乗り換えるつもりだったが、
各駅停車に乗るべきところを誤って急行に乗ってしまった。
自由が丘の次の急行停車駅で降り、反対方向の電車で一駅戻った駅が
つばめちゃんの目的地である。

この目的地の駅名を日本語で答えよ。
"""

answer = generate(prompt, max_new_tokens=64)
print("【44 対話】")
print(answer)
