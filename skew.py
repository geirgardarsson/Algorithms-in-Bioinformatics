import sys
import collections

dna = sys.stdin.readline().strip()

s = collections.defaultdict(int)
diff = 0

for i in range(len(dna)):
    if dna[i] == 'G':
        diff += 1
    if dna[i] == 'C':
        diff -= 1

    s[i] = diff

m = min(s.items(), key=lambda a:a[1])[1]

out = []

for x in sorted(s):
    if s[x] == m:
        out.append(x+1)

print(*out)

