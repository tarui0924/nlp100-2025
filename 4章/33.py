import CaboCha

text = "メロスは激怒した。"

c = CaboCha.Parser()
tree = c.parse(text)

chunks = {}
for i in range(tree.chunk_size()):
    ch = tree.chunk(i)
    surf = ""
    for j in range(ch.token_pos, ch.token_pos + ch.token_size):
        tok = tree.token(j)
        surf += tok.surface
    chunks[i] = {"dst": ch.link, "surface": surf}

for i, ch in chunks.items():
    if ch["dst"] != -1:
        print(f"{ch['surface']}\t{chunks[ch['dst']]['surface']}")
