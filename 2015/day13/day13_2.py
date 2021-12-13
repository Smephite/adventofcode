import sys, os
sys.path.append(os.path.abspath("."))
import aoc

graph = {}

for l in aoc.aoc():
    [f1, _, direction, num, _, _, _, _, _, _, f2] = l.split(" ")
    
    f2 = f2[0:-1]
    num = int(num)
    if direction == "lose":
        num*=-1
    
    if f1 in graph:
        graph[f1][f2] = num
    else:
        graph[f1] = {f2: num}

def find_shortest_path(graph, full_graph, starting, depth=0):

    if len(graph) == 1 and starting in graph:
        return 0

    assert(len(graph) != 1)

    new_graph = dict(map(lambda b: (b, graph[b]), filter(lambda b : b != starting, graph.keys())))

    cons = graph[starting]

    happyness = 0
    for con in list(filter(lambda b : b in graph, cons.keys())):        
        happyness = max(happyness, find_shortest_path(new_graph, full_graph, con, depth+1) + cons[con] + full_graph[con][starting])

    return happyness


dists = []

for starting in graph.keys():
    dist = find_shortest_path(graph, graph, starting)
    dists.append(dist)

print(f"The most increase in happieness is {max(dists)}.")