import sys, os, hashlib
sys.path.append(os.path.abspath(".."))
from aoc import aoc

input = aoc.aoc()[0]
number = 1
while hashlib.md5((input + str(number)).encode()).hexdigest()[0:5] != '00000':
    number+=1
print(f"The required hash number is {number}")