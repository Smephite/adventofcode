import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

floor = 0

for c in list(aoc.aoc()[0]):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
print(f"Santa ends up on floor {floor}")