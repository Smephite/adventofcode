import sys, os
sys.path.append(os.path.abspath("."))
import aoc

import re

input = aoc.aoc()[0]

chunks = re.split('[^\d-]', input)

sum = sum(map(lambda x : int(x), filter(lambda x : x != '', chunks)))

print(f"The sum is {sum}")