#06.集合
def n_gram(text,n):
  return [text[i:i+n] for i in range(len(text) - n + 1)]

str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(n_gram(str1,2))
Y = set(n_gram(str2,2))
union = X | Y
intersection = X & Y
difference = X - Y
print(f'X :{X} Y :{Y}\n')
print(f'X | Y :{union}\nX & Y :{intersection}\nX - Y :{difference}\n')

print('se in X' if 'se' in X else 'se not in X')
print('se in Y' if 'se' in Y else 'se not in Y')