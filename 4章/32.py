import MeCab

text = """
メロスは激怒した。
必ず、すの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮らして来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

tagger = MeCab.Tagger()
morphemes = []

for line in text.strip().split("\n"):
    node = tagger.parseToNode(line)
    while node:
        f = node.feature.split(",")
        morphemes.append(
            {"surface": node.surface, "pos": f[0], "pos1": f[1]}
        )
        node = node.next

for i in range(len(morphemes) - 2):
    a, no, b = morphemes[i : i + 3]
    if (
        a["pos"] == "名詞"
        and no["surface"] == "の"
        and no["pos"] == "助詞"
        and b["pos"] == "名詞"
    ):
        print(a["surface"] + "の" + b["surface"])
