#05.n-gram
def n_gram(text,n):
  #nずつ取り出す
  return [text[i:i+n] for i in range(len(text) - n + 1)]

text = "I am an NLPer"
char_seq = text.replace(' ','')
#文字2-gram
print(n_gram(char_seq, 2))
sentence = text.split()
#単語2-gram
print(n_gram(sentence, 2))