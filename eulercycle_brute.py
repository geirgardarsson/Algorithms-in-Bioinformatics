import sys
import random
from collections import defaultdict

inputs = [line.strip() for line in sys.stdin]

graph = defaultdict(list)
edges = []

for path in inputs:
    nodes = path.split("->")

    a = int(nodes[0])
    b = nodes[1].split(",")

    for node in b:
        node = int(node)
        graph[a].append(int(node))
        edges.append(str(a)+'-'+str(node))
        

cycles = []
maxvisited = 0

def traverseDown(node, cycle, visited, m):
    global maxvisited

    if m > maxvisited:
        maxvisited = m
        print(len(visited), node)

    if len(visited) == len(edges):
        cycles.append(cycle)

    else:
        for e in graph[node]:
            edge = str(node)+'-'+str(e)

            if edge not in visited:

                nextcycle = cycle[:] + [e]
                nextnode = e
                newvisit = visited[:] + [edge]

                traverseDown(nextnode, nextcycle, newvisit, m+1)


start = random.choice(list(graph.keys()))
traverseDown(start, [start], [], 0)

print("->".join(list(map(str, random.choice(cycles)))))

