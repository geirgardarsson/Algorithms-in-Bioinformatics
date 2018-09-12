import sys
import utils as u
import numpy as np
import collections


def calcprob(kmer, matrix):
    d = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }

    prob = 1

    for i in range(len(kmer)):
        prob *= matrix[d[kmer[i]]][i]

    return prob


dna = sys.stdin.readline().strip()
k = int(sys.stdin.readline().strip())

pr = []

for line in sys.stdin:
    pr.append([float(i) for i in line.strip().split(' ')])

pr = np.asarray(pr)
probs = []

for i in range(len(dna)-k+1):
    probs.append((calcprob(dna[i:i+k], pr), dna[i:i+k]))

m = max(probs, key=lambda a:a[0])[1]

print(m)

