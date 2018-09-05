import itertools

comb = itertools.combinations_with_replacement 


def hammlen(string1, string2, max):
    h = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            h += 1
            if h > max:
                break

    return h

def combinations(string, d):
    s = list(comb(string,d))
    s = list(map(lambda a:"".join(list(a)),s))

    return s

