import sys
import numpy as np
import string
from collections import defaultdict


def build(matname):
    mat = defaultdict(int)
    txtfile = open(matname + ".txt", "r")

    s = [line.strip().split(" ") for line in txtfile]
    s = [list(filter(lambda a: len(a) != 0, x)) for x in s]

    letters = s.pop(0)

    for x in s:
        x.pop(0)

    for i in range(0, len(s)):
        for j in range(0, len(s)):
            mat[letters[i] + letters[j]] = int(s[i][j])

    return mat


