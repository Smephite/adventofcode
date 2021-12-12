import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

nice_strings = 0

for string in aoc.aoc():
    repeats = any([string[i] == string[i+2] for i in range(len(string)-2)])
    repeats_pair = any([(string.count(string[i:i+2])>=2) for i in range(len(string)-2)])
    
    if repeats and repeats_pair:
        nice_strings +=1
        
    
print(f"There are {nice_strings} nice strings")