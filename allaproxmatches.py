import sys

pattern = sys.stdin.readline().strip()
dna = sys.stdin.readline().strip()
d = int(sys.stdin.readline().strip())

def hammlen(x,y):
    h = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            h += 1

    return h

out = []

for i in range(len(dna) - len(pattern)):
    h = hammlen(pattern, dna[i:i+len(pattern)])
    if h <= d:
        out.append(i)

print(*out)

