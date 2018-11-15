import sys
import random
from collections import defaultdict

inputs = [line.strip() for line in sys.stdin]
selected_graph = defaultdict(list)

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
    global selected_graph

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

print("->".join(list(map(str, eulerpath))))

