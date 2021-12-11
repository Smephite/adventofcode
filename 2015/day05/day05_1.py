import sys, os
sys.path.append(os.path.abspath(".."))
from aoc import aoc

nice_strings = 0

for string in aoc.aoc():
    vowls = 0
    last_c = ''
    double = False
    for c in string:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowls+=1
        if c == last_c:
            double = True
        last_c = c
    naughty_words = list(filter(lambda x: x, map(lambda x: x in string, ['ab', 'cd', 'pq', 'xy'])))
    nice = vowls>=3 and double and len(naughty_words) == 0
    if nice:
        nice_strings += 1
print(f"There are {nice_strings} nice strings")