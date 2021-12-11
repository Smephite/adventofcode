import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

sum_ribbon = 0

for present in aoc.aoc():
    [l, w, h] = list(map(lambda x: int(x), present.split("x")))
    volume = l*w*h
    perimeters = [2*l+2*w, 2*w+2*h, 2*h+2*l]
    sum_ribbon += volume + min(perimeters)

print(f"The length of ribbon needed is {sum_ribbon} ft")