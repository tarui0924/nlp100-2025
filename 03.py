#03.円周率

raw_text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

text = raw_text.replace(".", "").replace(",", "")

# ans = [len(w) for w in text.split()]

words = text.split()
ans = []
for w in words:
    ans.append(len(w))

print(ans)
