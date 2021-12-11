import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

nice_strings = 0

for string in aoc.aoc():
    
print(f"There are {nice_strings} nice strings")