import sys, os
sys.path.append(os.path.abspath("."))
import aoc


lights = [[0 for _ in range(1000)] for _ in range(1000)]


for line in aoc.aoc():
    instructions = line.split(" ")

    [x_to, y_to] = list(map(lambda x: int(x), instructions[-1].split(",")))
    [x_from, y_from] = list(map(lambda x: int(x), instructions[-3].split(",")))
    
    for x in range(x_from, x_to+1):
        for y in range(y_from, y_to+1):            
            if instructions[0] == 'toggle':
                lights[x][y] += 2
            elif instructions[0] == 'turn':
                if instructions[1] == 'on':
                    lights[x][y] += 1
                else:
                    lights[x][y] = max(lights[x][y]-1, 0)

print(f"The total brightness is {sum(map(lambda line: sum(list(filter(lambda light: light, line))), lights))}.")