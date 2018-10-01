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

'''
input:  two strings of equal length
output: hamming distance between them
'''
def hammlen(string1, string2):
    h = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            h += 1

    return h


'''
input:  integer k
output: list of all k-mer permutations
'''
def allkmers(k):
    kmers = list(it.product("ACGT", repeat=k))
    return [''.join(x) for x in kmers]



'''
input:  list of strings and integer k
output: all k-mer patterns in the strings
'''
def kpatterns(arr, k):
    patterns = []
    
    for dna in arr:
        for i in range(len(dna)-k+1):
            patterns.append(dna[i:i+k])

    return list(set(patterns))


'''
input:  dna: list of strings
        k  : k-mer length
        d  : maximum hamming distance

output: list of all kmers from dna, with hamming
        distance of most d
'''
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


'''
input:  list of strings (motifs)
output: score of given motifs
'''
def calcscore(arr):
    arr = np.asarray([list(x) for x in arr])
    score = arr.shape[0] * arr.shape[1]

    for i in range(arr.shape[1]):
        col = ''.join(arr[:,i])
        m = Counter(col).most_common(1)[0]
        score -= m[1]

    return score


'''
input:  kmer, profile matrix
output: probability of the consensus string 
'''
def calcprob(kmer, matrix):
    prob = 1

    for i in range(len(kmer)):
        prob *= matrix[di[kmer[i]]][i]

    return prob


'''
input:  dna: strings
        k  : k-mer length
        pr : profile matrix
output: most probable consensus string from dna
'''
def profilemostprobstring(dna, k, pr):
    probs = []

    for i in range(len(dna)-k+1):
        x = dna[i:i+k]
        probs.append((calcprob(x,pr),x))

    return max(probs, key=lambda a:a[0])[1]
    

'''
input:  dna: strings
        k: kmer length
        pr: profile matrix
output: random kmer from dna, chosen
        with the profile weights
'''
def randstringfromprofile(dna, k, pr):
    kmers = []
    probs = []

    for i in range(len(dna)-k+1):
        x = dna[i:i+k]
        kmers.append(x)
        probs.append(calcprob(x,pr))

    return np.random.choice(kmers,1,probs)[0]


'''
input:  list of strings (motifs)
        psecount, boolean if pseudocounts should
        be added. (optional, default false)
output: profile matrix from the motifs
'''
def makeprofile(motifs, psecount=False):
    motifs = np.asarray([list(x) for x in motifs])
    motifs = np.transpose(motifs)

    counts = [Counter(x) for x in motifs]

    profiles = [
        [c['A'],c['C'],c['G'],c['T']]
        for c in counts
    ]

    if psecount:
        profiles = addpseudocounts(profiles)

    j = sum(profiles[0])

    divide = lambda a: a/j
    vdivide = np.vectorize(divide)

    profiles = [
        vdivide(x)
        for x in profiles
    ]

    profiles = np.transpose(np.asarray(profiles))

    return profiles


'''
input:  profile matrix
output: profile with added pseudocounts
'''
def addpseudocounts(profile):
    inc = lambda a: a+1
    vinc = np.vectorize(inc)

    profile = [vinc(x) for x in profile]

    return np.asarray(profile)


