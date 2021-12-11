import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

pos = (0, 0)
pos_robo = pos
houses = [pos]

directions = {'>': (1, 0), '<': (-1, 0), 'v': (0, -1), '^': (0, 1)}

turn = False

for d in aoc.aoc()[0]:
    if turn:
        pos = (pos[0]+directions[d][0], pos[1]+directions[d][1])
        houses.append(pos)
    else:
        pos_robo = (pos_robo[0]+directions[d][0], pos_robo[1]+directions[d][1])
        houses.append(pos_robo)
    turn = not turn

unique_houses = list(set(houses))
print(f"Santa visits {len(unique_houses)} house at least once.")