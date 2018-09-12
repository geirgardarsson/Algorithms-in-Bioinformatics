import sys
import utils as u
import numpy as np
import collections

def minhamm(text, pattern):
    l = []

    for i in range(len(text)-len(pattern)+1):
        h = u.hammlen(text[i:i+len(pattern)], pattern)

        l.append((h,i))

    return min(l, key=lambda a:a[0])


k = int(sys.stdin.readline().strip())

dna = []

for line in sys.stdin:
    dna.append(line.strip())

allk = u.allkmers(k)

summs = collections.defaultdict(int)

for kmer in allk:
    s = 0
    
    for d in dna:
        s += minhamm(d,kmer)[0]

    summs[kmer] = s

print(min(summs.items(), key=lambda a:a[1])[0])

