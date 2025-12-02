import gzip
import json
from collections import Counter
import MeCab
import matplotlib.pyplot as plt

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
    n = tag.parseToNode(t)
    while n:
        if n.surface:
            cnt[n.surface] += 1
        n = n.next

freq = [f for _, f in cnt.most_common()]
rank = range(1, len(freq) + 1)

plt.loglog(rank, freq)
plt.xlabel("rank")
plt.ylabel("frequency")
plt.title("Zipf's law (Wikipedia Japanese)")
plt.savefig("zipf.png")
# plt.show()  # GUI環境ならこっちでもOK
