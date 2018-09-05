import sys

dna1 = sys.stdin.readline().strip()
dna2 = sys.stdin.readline().strip()

h = 0

for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        h += 1

print(h)

