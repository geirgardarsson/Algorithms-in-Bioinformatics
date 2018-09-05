import sys
import utils
import collections
from itertools import product


dna = sys.stdin.readline().strip()
inputs = sys.stdin.readline().strip()
inputs = inputs.split(" ")

hammlen = utils.hammlen

k = int(inputs[0])
d = int(inputs[1])

allkmers = list(product("ACGT", repeat=k))
allkmers = [''.join(x) for x in allkmers]

s = collections.defaultdict(int)

for kmer in allkmers:
    for j in range(len(dna) - k + 1):
        h = hammlen(kmer, dna[j:j+k], d)
        if h <= d:
            s[kmer] += 1

m = max(s.items(), key=lambda a:a[1])[1]

out = []

for x in s:
    if s[x] == m:
        out.append(x)

print(*out)

