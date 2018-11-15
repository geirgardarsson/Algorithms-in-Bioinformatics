import sys
from collections import defaultdict
from graphutils import eulerp, debruj 

k = int(sys.stdin.readline().strip())
kmers = [line.strip() for line in sys.stdin]



def kmerKeys(kmers):
    out = []

    for kmer in kmers:
        out.append(kmer[:-1])
        out.append(kmer[1:])

    return out


d = debruj(kmers)

kmersToNum = defaultdict(str)
numToKmers = defaultdict(str)

kKeys = kmerKeys(kmers)


for i, kmer in enumerate(kKeys):
    numToKmers[i] = kmer
    kmersToNum[kmer] = i

graph = []

for key in d:
    left = kmersToNum[key]
    right = [str(kmersToNum[x]) for x in d[key]]

    graph.append(str(left) + " -> " + ",".join(right))


epath = eulerp(graph).split("->")

epath = [numToKmers[int(x)] for x in epath][::-1]
string = epath[0][:-1] + "".join(k[-1] for k in epath)

print(string)

