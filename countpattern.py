import sys

dna = sys.stdin.readline().strip()
pattern = sys.stdin.readline().strip()

count = 0
i = 0

while i < (len(dna) - len(pattern)):
    if dna[i:i+len(pattern)] == pattern:
        count += 1
    i += 1

print(count)

