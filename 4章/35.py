import CaboCha

text = "メロスは激怒した。"

c = CaboCha.Parser()
tree = c.parse(text)

for i in range(tree.chunk_size()):
    ch = tree.chunk(i)
    surf = ""
    for j in range(ch.token_pos, ch.token_pos + ch.token_size):
        surf += tree.token(j).surface
    print(f"[{i}] {surf} -> {ch.link}")
