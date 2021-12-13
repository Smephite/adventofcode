import sys, os
sys.path.append(os.path.abspath("."))
import aoc

aunt_list = False

hints = {}
aunts = {}

def matches(name, real_value, hint_value):
    less = ['pomeranians', 'goldfish']
    more = ['cats', 'trees']
    
    if name in less:
        return real_value < hint_value
    elif name in more:
        return real_value > hint_value
    else:
        return real_value == hint_value

for l in aoc.aoc():
    if l == "":
        aunt_list = True
        continue
    
    if aunt_list:
        splits = l.split(": ")
        name = splits[0]
        infos = ": ".join(splits[1:])
        infos = infos.split(",")

        info_list = {}

        for info in infos:
            [property_name, value] = info.split(": ")
            info_list[property_name.replace(" ", "")] = int(value)
        aunts[name] = info_list
    else:
        [property_name, value] = l.split(": ")
        hints[property_name] = int(value)

possible_aunts = list(filter(lambda aunt_name: all(map(lambda property: property not in aunts[aunt_name] or matches(property, aunts[aunt_name][property], hints[property]), hints.keys())), aunts.keys()))

assert(len(possible_aunts) == 1)

print("We actually got the gift from", possible_aunts[0])