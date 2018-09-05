import sys
import collections

dna = sys.stdin.readline().strip()
inputs = sys.stdin.readline().strip()
inputs = inputs.split(" ")

k = int(inputs[0])
L = int(inputs[1])
t = int(inputs[2])

kmers = [] # return values

i = 0
while i <= len(dna) - L:
    
    frag = dna[i:i+L]
    count = 0
    j = 0

    s = collections.defaultdict(int)

    while j <= len(frag) - k:
        km = frag[j:j+k]
        s[km] += 1
        j += 1
    
    m = (max(s.items(), key=lambda a:a[1]))[1]
    
    for x in sorted(s):
        if s[x] == m and m == t:
            if x not in kmers:
                kmers.append(x)

    i += 1

print(*kmers)

