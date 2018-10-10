import sys
import numpy as np
from collections import defaultdict


inputs = [line.strip() for line in sys.stdin]

source = int(inputs.pop(0))
sink   = int(inputs.pop(0))

dag = defaultdict(list)

for path in inputs:
    nodes = path.split("->")

    a = int(nodes[0])
    b = nodes[1].split(":")
    w = int(b[1])
    b = int(b[0])

    # path a -> b, with weight w
    dag[a].append((b,w))


paths = []


def traverseDown(node, p, w):
    if len(node) == 0 and p[-1] == sink:
        paths.append((p, w))

    else:
        # e = (node key, weight into node)
        for e in node:
            nextp = p[:]
            nextp.append(e[0])
            nextw = w + e[1]
            nextnode = dag[nextp[-1]]

            traverseDown(nextnode, nextp, nextw)
           

traverseDown(dag[source], [source], 0)


m = max(paths, key=lambda a:a[1])

print(m[1])
print("->".join(str(x) for x in m[0]))

