import CaboCha

text = """
メロスは激怒した。
メロスは、村の牧人である。
"""

c = CaboCha.Parser()
tree = c.parse(text)

chunks = []
for i in range(tree.chunk_size()):
    ch = tree.chunk(i)
    surf = ""
    for j in range(ch.token_pos, ch.token_pos + ch.token_size):
        surf += tree.token(j).surface
    chunks.append({"dst": ch.link, "surface": surf})

for i, ch in enumerate(chunks):
    if "メロス" in ch["surface"] and ch["dst"] != -1:
        print("主語:", ch["surface"], "/ 述語:", chunks[ch["dst"]]["surface"])
