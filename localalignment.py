import sys
import numpy as np
import matrixbuilder

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

s = np.zeros((len(a)+1, len(b)+1))

pam250 = matrixbuilder.build("pam250")


def calcweight(a,b):
    
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):

            s[i][j] = max(
                s[i-1][j] - 5,
                s[i][j-1] - 5,
                s[i-1][j-1] + pam250[ a[i-1] + b[j-1] ],
                0
            )

def outputAlignment(a,b,e):
    newa = ''
    newb = ''
    i = e[0]
    j = e[1]

    while i > 0 and j > 0:

        if s[i][j] == s[i-1][j-1] + pam250[ a[i-1] + b[j-1] ]: 
            newa += a[i-1]
            newb += b[j-1]
            i -= 1
            j -= 1

        elif s[i][j] == s[i-1][j] - 5:
            newa += a[i-1]
            newb += '-'
            i -= 1

        elif s[i][j] == s[i][j-1] - 5:
            newa += '-'
            newb += b[j-1]
            j -= 1

        else:
            break
        

    return [newa[::-1], newb[::-1]]



calcweight(a,b)
endpoint = np.unravel_index(s.argmax(), s.shape)
alignment = outputAlignment(a,b, endpoint)
print(int(s[endpoint[0]][endpoint[1]]))
print(alignment[0])
print(alignment[1])

