import sys

pattern = sys.stdin.readline().strip()
dna = sys.stdin.readline().strip()

out = []
i = 0

while i < len(dna) - len(pattern):
    if dna[i:i+len(pattern)] == pattern:
        out.append(i)
    
    i += 1

print(*out)

