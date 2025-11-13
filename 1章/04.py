#04.元素記号

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = text.replace(".", "").split()

ans_dict = {}
for i, w in enumerate(words, 1):
    if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        x = w[0]
        ans_dict[x] = i
    else:
        x = w[:2]
        ans_dict[x] = i

print(ans_dict)
