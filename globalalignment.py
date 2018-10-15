import sys
import numpy as np
import matrixbuilder

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

s = np.zeros((len(a)+1, len(b)+1))


blosum62 = matrixbuilder.build("blosum62")


'''
Breaks for huge inputs
'''
def calcweight_recursive(i,j):
    if i == 0 and j == 0:
        return 0

    x = -float("inf")
    y = -float("inf")
    z = -float("inf")

    if i > 0:
        if s[i][j] > 0:
            x = s[i][j]
        else:
            x = calcweight(i-1,j) - 5

    if j > 0:
        if s[i][j] > 0:
            y = s[i][j]
        else:
            y = calcweight(i,j-1) - 5


    if i > 0 and j > 0:
        if s[i][j] > 0:
            z = s[i][j]
        else:
            z = calcweight(i-1,j-1) + blosum62[a[i-1] + b[j-1]]

    s[i][j] = max(x,y,z)

    return max(x,y,z)


def calcweight(a,b):

    for i in range(1, len(a)+1):
        s[i][0] = s[i-1][0] - 5

    for j in range(1, len(b)+1):
        s[0][j] = s[0][j-1] - 5

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):

            s[i][j] = max(
                s[i-1][j] - 5,
                s[i][j-1] - 5,
                s[i-1][j-1] + blosum62[ a[i-1] + b[j-1] ]
            )
            

def outputAlignment(a,b):
    newa = ''
    newb = ''
    i = len(a)
    j = len(b)

    while i > 0 or j > 0:
        
        if s[i][j] == s[i-1][j] - 5 and i > 0:
            newa += a[i-1]
            newb += '-'
            i -= 1

        elif s[i][j] == s[i][j-1] - 5 and j > 0:
            newa += '-'
            newb += b[j-1]
            j -= 1

        else:
            newb += b[j-1]
            newa += a[i-1]
            i -= 1
            j -= 1

    return [newa[::-1], newb[::-1]]




calcweight(a, b)
alignment = outputAlignment(a,b)
#print(s)
print(int(s[len(a)][len(b)]))
print(alignment[0])
print(alignment[1])

