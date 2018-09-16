import sys
import utils as u

inputs = sys.stdin.readline().strip().split(" ")
k = int(inputs[0])
t = int(inputs[1])

dna = []

for line in sys.stdin:
    dna.append(line.strip()) 


bestmotifs = [a[0:k] for a in dna] 
d = dna[0]

for i in range(len(d)-k+1):
    motifs = [d[i:i+k]]

    for j in range(1,t):
        p = u.makeprofile(motifs)
        motifs.append(u.profilemostprobstring(dna[j],k,p))


    if u.calcscore(motifs) < u.calcscore(bestmotifs):
        bestmotifs = motifs


for s in bestmotifs:
    print(s)

