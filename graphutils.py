import sys
from collections import defaultdict
import random


def eulerp(inputs):

    sys.setrecursionlimit(5000)

    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    

    edges = []
    sources = []

    for path in inputs:
        nodes = path.split("->")

        a = int(nodes[0])
        b = nodes[1].split(",")

        for node in b:
            node = int(node)
            graph[a].append(int(node))
            edges.append((a,node))
            sources.append(node)

            reverse_graph[node].append(a)


    def traverseGraph(nodes, path):

        if len(nodes) == 0:
            return path
        else:
            nextnode = random.choice(nodes)

            # Mark the path (by removing it)
            selected_graph[path[-1]].remove(nextnode)

            return traverseGraph(selected_graph[nextnode], path + [nextnode])


    # Determine if the endpoint is a source or a sink
    left = set(graph.keys())
    right = set(sources)

    source = list(left - right)[0] if len(left) > len(right) else list(right - left)[0]
    selected_graph = graph if source in left else reverse_graph

    eulerpath = traverseGraph(selected_graph[source], [source])

    while len(eulerpath) < len(edges):

        left = [
            x[0] for x in
            filter(lambda a: len(a[1]) > 0, list(selected_graph.items()))
        ]

        nextstart = random.choice(list(set(eulerpath) & set(left)))
        path = traverseGraph(selected_graph[nextstart], [nextstart])
        i = eulerpath.index(nextstart)

        eulerpath = eulerpath[0:i] + path + eulerpath[i+1:]


    if len(right) > len(left):
        eulerpath = eulerpath[::-1]

    return("->".join(list(map(str, eulerpath))))


def debruj(kmers):
    sources = [x[:-1] for x in kmers]
    destinations = [x[1:] for x in kmers]

    debruijn = defaultdict(list)
    sourcecount = defaultdict(int)

    for s in sources:
        sourcecount[s] += 1

    for s in sources:
        for d in destinations:

            if s[1:] == d[:-1] and sourcecount[s] > 0 and s+d[-1] in kmers:
                debruijn[s].append(d)
                sourcecount[s] -= 1

    return debruijn
    
