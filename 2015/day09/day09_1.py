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
        graph[pos_to] = {pos_to: int(dist)}

print(graph)
# TODO
