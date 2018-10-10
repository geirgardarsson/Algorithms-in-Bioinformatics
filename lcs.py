import sys
import numpy as np

sys.setrecursionlimit(5000)

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip() 

s = np.zeros((len(a)+1, len(b)+1))
backtrack = np.chararray((len(a)+1, len(b)+1), unicode=True)
backtrack[:] = '.'


def calcweight(i,j):
    if i == 0 and j == 0:
        return 0

    x = -float("inf")
    y = -float("inf")
    z = -float("inf")

    if i > 0:
        if s[i][j] > 0:
            x = s[i][j]
        else:
            x = calcweight(i-1,j)

    if j > 0:
        if s[i][j] > 0:
            y = s[i][j]
        else:
            y = calcweight(i,j-1)

    if i > 0 and j > 0 and a[i-1] == b[j-1]:
        if s[i][j] > 0:
            z = s[i][j]
        else:
            z = calcweight(i-1,j-1) + 1

    s[i][j] = max(x,y,z)

    return max(x,y,z) 



def calcLCS(a,b):
    revlcs = ''
    i = len(a)
    j = len(b)

    while i > 0 and j > 0:

        if s[i][j] == s[i-1][j-1] + 1 and a[i-1] == b[j-1]:
            revlcs += a[i-1]
            i -= 1
            j -= 1

        elif s[i][j] == s[i-1][j]:
            i -= 1

        elif s[i][j] == s[i][j-1]:
            j -= 1

        else:
            i -= 1
            j -= 1

    return revlcs[::-1]


calcweight(len(a), len(b))
lcs = calcLCS(a, b)
print(lcs)

