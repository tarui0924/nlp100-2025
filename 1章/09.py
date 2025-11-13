#09.Typoglycemia
import random
text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(f"原文: {text}")
text = text.split(" ")

def shuffle(text):
    random_words = []
    for word in text:
        start = word[0]
        end = word[-1]
        if len(word) <= 4:
            random_words.append(word)
        else:
            others = random.sample(word[1:-1], len(word[1:-1]))
            random_words.append("".join([start] + others + [end]))
    result = " ".join(random_words)
    return result

print(f"ランダム文: {shuffle(text)}")