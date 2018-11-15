import sys

perm = sys.stdin.readline().strip()[1:-1].split(" ")

indexes = [int(x[1:]) for x in perm]


def rev(c):
    if c[0] == "+":
        return "-" + c[1:]
    else:
        return "+" + c[1:]


def flip(p):
    return list(map(rev,p[::-1]))


sequences = []
i = 0

while i < len(perm):

    if int(perm[i][1:]) == i+1 and perm[i][0] == "+":
        i += 1

    else:
        j = indexes.index(i + 1)

        perm = perm[0:i] + flip(perm[i:j+1]) + perm[j+1:] 
        indexes = indexes[0:i] + indexes[i:j+1][::-1] + indexes[j+1:]
        
        sequences.append(perm)

        i = 0

for seq in sequences:
    print("(" + " ".join(seq) + ")")

