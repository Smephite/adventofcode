import sys, os
sys.path.append(os.path.abspath("."))
import aoc

graph = {}

for line in aoc.aoc():
    [pos_from, _, pos_to, _, dist] = line.split(" ")

    if pos_from in graph:
        graph[pos_from][pos_to] = int(dist)
    else:
        graph[pos_from] = {pos_to: int(dist)}

    if pos_to in graph:
        graph[pos_to][pos_from] = int(dist)
    else:
        graph[pos_to] = {pos_from: int(dist)}


def find_shortest_path(graph, starting, depth=0):

    if len(graph) == 1 and starting in graph:
        return 0

    assert(len(graph) != 1)

    new_graph = dict(map(lambda b: (b, graph[b]), filter(lambda b : b != starting, graph.keys())))

    cons = graph[starting]

    min_dist = 0
    for con in list(filter(lambda b : b in graph, cons.keys())):        
        min_dist = max(min_dist, find_shortest_path(new_graph, con, depth+1) + cons[con])

    assert(min_dist != 0)
    return min_dist


dists = []

for starting in graph.keys():
    dist = find_shortest_path(graph, starting)
    dists.append(dist)

print(f"The distance of the longest route is {max(dists)}.")