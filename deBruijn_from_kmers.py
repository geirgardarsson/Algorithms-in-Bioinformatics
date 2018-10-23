import sys
from collections import defaultdict 

kmers = [line.strip() for line in sys.stdin]

sources = [x[:-1] for x in kmers]
destinations = [x[1:] for x in kmers]

debruijn = defaultdict(list)
sourcecount = defaultdict(int)

for s in sources:
    sourcecount[s] += 1

for s in sources:
    for d in destinations:

        if s[1:] == d[:-1] and sourcecount[s] > 0 and s+d[-1] in kmers:
            debruijn[s].append(d)
            sourcecount[s] -= 1


for key in sorted(debruijn):
    print(key, '->', ",".join(sorted(debruijn[key])))

