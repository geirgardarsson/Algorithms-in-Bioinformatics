import itertools as it
import numpy as np
from collections import Counter

comb = it.combinations_with_replacement 


#dna indexes
di = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }

def hammlen(string1, string2, m=0, fast=False):
    h = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            h += 1
            if fast and h > m:
                break

    return h


def combinations(string, d):
    s = list(comb(string,d))
    s = list(map(lambda a:"".join(list(a)),s))

    return s


def allkmers(k):
    kmers = list(it.product("ACGT", repeat=k))
    return [''.join(x) for x in kmers]


def kpatterns(arr, k):
    patterns = []
    
    for dna in arr:
        for i in range(len(dna)-k+1):
            patterns.append(dna[i:i+k])

    return list(set(patterns))


def aproxkmers(dna,k,d):
    patterns = kpatterns(dna,k)

    allk = allkmers(k)

    apatterns = []

    for kmer in allk:
        for p in patterns:
            if hammlen(kmer, p, d) <= d:
                apatterns.append(kmer)


    return list(set(apatterns))


'''
input: np.2darray of characters

output: tuple of consensus string and its score

----------------
to convert list of strings to np.2darray of characters:
    2darr = np.asarray([list(x) for x in dna])

'''
def conscore(arr):
    cons = ""
    score = 0

    for i in range(arr.shape[1]):
        col = ''.join(arr[:,i])
        m = Counter(col).most_common(1)[0]
        cons  += m[0]
        score += m[1]
        
    return (cons, score)


def calcscore(arr):
    arr = np.asarray([list(x) for x in arr])
    score = arr.shape[0] * arr.shape[1]

    for i in range(arr.shape[1]):
        col = ''.join(arr[:,i])
        m = Counter(col).most_common(1)[0]
        score -= m[1]

    return score


def calcprob(kmer, matrix):
    prob = 1

    for i in range(len(kmer)):
        prob *= matrix[di[kmer[i]]][i]

    return prob


def profilemostprobstring(dna, k, pr):
    probs = []

    for i in range(len(dna)-k+1):
        x = dna[i:i+k]
        probs.append((calcprob(x,pr),x))

    return max(probs, key=lambda a:a[0])[1]
    



def makeprofile(motifs):
    motifs = np.asarray([list(x) for x in motifs])
    j = motifs.shape[0]
    motifs = np.transpose(motifs)

    counts = [Counter(x) for x in motifs]

    profiles = [
        [c['A'],c['C'],c['G'],c['T']]
        for c in counts
    ]

    divide = lambda a: a/j
    vdivide = np.vectorize(divide)

    profiles = [
        vdivide(x)
        for x in profiles
    ]

    profiles = np.transpose(np.asarray(profiles))

    return profiles














