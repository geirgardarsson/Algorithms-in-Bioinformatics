import sys
from collections import defaultdict 

k = int(sys.stdin.readline().strip())
dna = sys.stdin.readline().strip()

kmers = [dna[i:i+k] for i in range(0, len(dna)-k+1)]

sources = [x[:-1] for x in kmers]
destinations = [x[1:] for x in kmers]

debruijn = defaultdict(list)

for i in range(len(sources)):
    debruijn[sources[i]].append(destinations[i])


for key in sorted(debruijn):
    print(key, '->', ",".join(sorted(debruijn[key])))

