import sys
import collections

dna = sys.stdin.readline().strip()

s = collections.defaultdict(int)

for e in dna:
    s[e] += 1

out = ""

for x in 'ACGT':
    out += str(s[x]) + " "

print(out)

