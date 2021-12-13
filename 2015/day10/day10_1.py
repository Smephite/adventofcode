import sys, os
sys.path.append(os.path.abspath("."))
import aoc

current_line = aoc.aoc()[0]

for _ in range(40):
    chars = []
    for c in list(current_line):
        if len(chars) == 0 or chars[-1][0] != c:
            chars.append((c, 1))
        else:
            chars[-1] = (chars[-1][0], chars[-1][1]+1)
    
    current_line = ""
    
    for c in chars:
        current_line += str(c[1]) + c[0]

print(len(current_line))
