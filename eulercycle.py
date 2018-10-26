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
        edges.append((a,node))
        

def traverseGraph(nodes, cycle):
    global graph

    if len(nodes) == 0:
        return cycle
    else:
        nextnode = random.choice(nodes)
        
        # Mark the path (by removing it)
        graph[cycle[-1]].remove(nextnode)

        return traverseGraph(graph[nextnode], cycle + [nextnode])
    

start = random.choice(list(graph.keys()))
eulercycle = traverseGraph(graph[start], [start])

while len(eulercycle) < len(edges):

    left = [
        x[0] for x in 
        filter(lambda a: len(a[1]) > 0, list(graph.items()))
    ]

    nextstart = random.choice(list(set(eulercycle) & set(left)))
    i = eulercycle.index(nextstart)
    eulercycle = eulercycle[i:] + eulercycle[1:i] + [nextstart]

    eulercycle = traverseGraph(graph[nextstart], eulercycle)


print("->".join(list(map(str, eulercycle))))

