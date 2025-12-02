import gzip
import json
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def iterarts(fname="jawiki-country.json.gz"):
    with gzip.open(fname, "rt", encoding="utf-8") as f:
        for l in f:
            j = json.loads(l)
            yield j.get("title", ""), j.get("text", "")

tag = MeCab.Tagger()

def tokenize_nouns(t):
    n = tag.parseToNode(t)
    r = []
    while n:
        f = n.feature.split(",")
        if f[0] == "名詞":
            r.append(n.surface)
        n = n.next
    return r

titles = []
docs = []

for tt, tx in iterarts():
    if "日本" in tt:        # 日本に関する記事
        titles.append(tt)
        docs.append(tx)

vectorizer = TfidfVectorizer(tokenizer=tokenize_nouns, use_idf=True)
X = vectorizer.fit_transform(docs)

tfidf_sum = np.asarray(X.sum(axis=0)).ravel()
indices = tfidf_sum.argsort()[::-1][:20]
terms = vectorizer.get_feature_names_out()

for idx in indices:
    print(terms[idx], tfidf_sum[idx])
