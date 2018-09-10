import sys
import collections
import utils as u

inputs = sys.stdin.readline().strip().split(" ")
k = int(inputs[0])
d = int(inputs[1])

dna = []

for line in sys.stdin:
    dna.append(line.strip())

dp = [] # dna patterns

for kmer in dna:
    for i in range(len(kmer)-k+1):
        dp.append(kmer[i:i+k])
        
dp = list(set(dp))

allk = u.allkmers(k)

patterns = []

for kmer in allk:
    for p in dp:
        if u.hammlen(kmer, p, d) <= d:
            patterns.append(kmer)

patterns = list(set(patterns))

output = []

for motif in patterns:
    inall = True

    for string in dna:
        instring = False

        for i in range(len(string)-k+1):
            if u.hammlen(motif, string[i:i+k], d) <= d:
                instring = True
                break
                
        if not instring:
           inall = False

    if inall:
        output.append(motif)


output = list(set(output))

print(*output)

