import sys, os
sys.path.append(os.path.abspath("."))
import aoc

total = 0

for line in aoc.aoc():
    num_chars = 0
    line = line[1:-1]
    
    i = 0
    while i < len(line):
        c = line[i]
        if c == '\\':
            if line[i+1] == 'x':
                i+=3
            else:
                i+=1
        num_chars+=1
        i+=1
    total += len(line)+2-num_chars
print(f"The answer is {total}")