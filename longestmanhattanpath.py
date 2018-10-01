import sys
import utils as u
import numpy as np


inputs = sys.stdin.readline().strip().split(" ")
n = int(inputs[0])
m = int(inputs[1])

maps = [line.strip() for line in sys.stdin]

down  = []
right = []

splt = maps.index("-")

for s in range(0, splt):
    down.append(maps[s])

for s in range(splt+1, len(maps)):
    right.append(maps[s])

parseint = lambda a: int(a)
pint = np.vectorize(parseint)

down = [x.split(" ") for x in down]
down = np.asarray([pint(x) for x in down])

right = [x.split(" ") for x in right]
right = np.asarray([pint(x) for x in right])

manhattan = np.zeros((n+1, m+1))


# function defined here so 
# the down and right arrays
# are accessable
def southoreast(i,j):
    if i == 0 and j == 0:
        return 0

    x = -float("inf")
    y = -float("inf")

    if i > 0:
        x = southoreast(i-1, j) + down[i-1][j]
    if j > 0:
        y = southoreast(i, j-1) + right[i][j-1]

    return max(x,y)

print(southoreast(n,m))

