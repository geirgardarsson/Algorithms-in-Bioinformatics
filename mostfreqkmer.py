import sys
import collections

dna = sys.stdin.readline().strip()
k = int(sys.stdin.readline().strip())

s = collections.defaultdict(int)
i = 0

while i < len(dna)-k+1:
    p = dna[i:i+k]
    s[p] += 1
    i += 1

m = (max(s.items(), key=lambda a:a[1]))[1]
out = ""

for x in sorted(s):
    if s[x] == m:
        out += x + " "

print(out)

