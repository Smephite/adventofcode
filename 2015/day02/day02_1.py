import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

sum_area = 0

for present in aoc.aoc():
    [l, w, h] = list(map(lambda x: int(x), present.split("x")))
    areas = [l*w, w*h, h*l]
    smallest = min(areas)
    area_needed = 2*sum(areas) + smallest

    sum_area += area_needed

print(f"The area needed is {sum_area} ft^2")