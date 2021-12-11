import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

floor = 0
i = 0
for c in list(aoc.aoc()[0]):
    i += 1
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
    
    if floor < 0:
        break

print(f"Santa ends up in the basement at {i}")