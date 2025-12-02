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

for line in text.strip().split("\n"):
    node = tagger.parseToNode(line)
    while node:
        f = node.feature.split(",")
        if f[0] == "動詞":
            print(node.surface, "→", f[6])
        node = node.next
