import sys, os
sys.path.append(os.path.abspath("."))
import aoc


lights = [[False for _ in range(1000)] for _ in range(1000)]


for line in aoc.aoc():
    instructions = line.split(" ")

    [x_to, y_to] = list(map(lambda x: int(x), instructions[-1].split(",")))
    [x_from, y_from] = list(map(lambda x: int(x), instructions[-3].split(",")))
    
    for x in range(x_from, x_to+1):
        for y in range(y_from, y_to+1):            
            if instructions[0] == 'toggle':
                lights[x][y] = not lights[x][y]
            elif instructions[0] == 'turn':
                if instructions[1] == 'on':
                    lights[x][y] = True
                else:
                    lights[x][y] = False

print(f"There are {sum(map(lambda line: len(list(filter(lambda light: light, line))), lights))} lights turned on.")