import itertools as it
from collections import Counter

comb = it.combinations_with_replacement 


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

