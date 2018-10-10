import sys
import utils as u
import random as r

inputs = sys.stdin.readline().strip().split(" ")
k = int(inputs[0])
t = int(inputs[1])


dna = [line.strip() for line in sys.stdin]

def randkmer(x):
    l = len(x) - k
    p = r.randint(0,l)
    return x[p:p+k] 
    

rkmers = [randkmer(s) for s in dna]

bestmotifs = rkmers[:]
motifs = rkmers[:]

i = 0

while i < 1:
    print()
    for m in motifs:
        print(m)
    print()

    p = u.makeprofile(motifs, True)

    for s in p:
        s = map("{0:.2f}".format, s)
        print(*s)
    print()

    motifs = [
        u.randstringfromprofile(s, k, p)
        for s in dna
    ]

    for m in motifs:
        print(m)
    print()

    if u.calcscore(motifs) < u.calcscore(bestmotifs):
        bestmotifs = motifs[:]

    i += 1

for s in bestmotifs:
    print(s)

