import sys, os
sys.path.append(os.path.abspath("."))
import aoc

import json

input = aoc.aoc()[0]
input = json.loads(input)

def sum_element(element):

    if isinstance(element, str):
        return 0
    if isinstance(element, int):
        return int(element)
    
    if isinstance(element, dict):
        if "red" in element.keys() or "red" in element.values():
            return 0
        element = element.values()

    return sum(map(lambda element: sum_element(element), element))

print("The sum excluding 'red' is:", sum_element(input))