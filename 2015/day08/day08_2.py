import sys, os
sys.path.append(os.path.abspath("."))
import aoc

total = 0

for line in aoc.aoc():
    num_chars = 0
    
    for c in line:
        if c in ['\\', '\n', '\"']:
            num_chars+=1
        num_chars+=1
    num_chars+=2
    
    total += num_chars-len(line)
print(f"The answer is {total}")