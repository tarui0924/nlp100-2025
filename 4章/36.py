import gzip
import json
from collections import Counter
import MeCab

def itertexts(fname="jawiki-country.json.gz"):
    with gzip.open(fname, "rt", encoding="utf-8") as f:
        for line in f:
            j = json.loads(line)
            t = j.get("text", "")
            if t:
                yield t

tag = MeCab.Tagger()
cnt = Counter()

for t in itertexts():
    node = tag.parseToNode(t)
    while node:
        if node.surface:
            cnt[node.surface] += 1
        node = node.next

for w, f in cnt.most_common(20):
    print(w, f)
