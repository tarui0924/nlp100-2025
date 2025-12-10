from common_llm import generate

questions = [
    {
        "q": "江戸幕府の対外政策について正しいものはどれか。\n"
             "A: 出島を通じたオランダとの貿易\n"
             "B: 日米修好通商条約の締結\n"
             "C: 士農工商の身分制の廃止\n"
             "D: 郵便制度の開始",
        "ans": "A",
    },
    {
        "q": "明治維新の中心人物として最も適切なのはどれか。\n"
             "A: 織田信長\n"
             "B: 西郷隆盛\n"
             "C: 足利義満\n"
             "D: 北条時宗",
        "ans": "B",
    },
]

correct = 0

for i, qu in enumerate(questions, 1):
    prompt = (
        qu["q"] +
        "\n\nもっとも正しい選択肢の記号（A,B,C,D）のうち1文字だけを答えよ。"
    )
    out = generate(prompt, max_new_tokens=8)
    print(f"Q{i} 出力:", out)

    # 先頭のアルファベットだけ拾う雑なパーサ
    pred = None
    for ch in out:
        if ch.upper() in ["A", "B", "C", "D"]:
            pred = ch.upper()
            break

    print("  予測:", pred, "/ 正解:", qu["ans"])
    if pred == qu["ans"]:
        correct += 1

accuracy = correct / len(questions)
print(f"\n正解数: {correct}/{len(questions)}  正解率: {accuracy:.2f}")
