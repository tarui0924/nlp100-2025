#08.暗号文
def cipher(lst):#暗号化を行う関数
  for i,c in enumerate(lst):
    # 英字 and 小文字
    if lst[i].isalpha() and lst[i].islower():
      # ord :unicode変換
      lst[i] = chr(219 - ord(lst[i]))
  return lst


text = "The quick brown fox jumps over the lazy dog."
print("原文：", text)
encode = cipher(list(text))
print("暗号化：", "".join(encode))
decode = cipher(encode)
print("複合化：", "".join(encode))