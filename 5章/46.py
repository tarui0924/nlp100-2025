from common_llm import generate

prompt = """
適当なお題を自分で一つ決め、そのお題に関する川柳を10個作成せよ。
出力は「お題：◯◯」のあとに、1行に1つずつ川柳を書くこと。
"""

answer = generate(prompt, max_new_tokens=256)
print("【46 川柳】")
print(answer)
