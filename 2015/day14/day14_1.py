import sys, os
sys.path.append(os.path.abspath("."))
import aoc

reindeers = {}

for l in aoc.aoc():
    [name, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _] = l.split(" ")
    reindeers[name] = {'speed': int(speed), 'flying_time': int(time), 'rest_time': int(rest), 'resting_left': 0, 'flying_left': int(time), 'dist_traveled': 0}


for t in range(0, 2503):
    for reindeer in reindeers.keys():
        name = reindeer
        info = reindeers[name]
        if info['flying_left'] > 0:
            reindeers[name]['flying_left'] = info['flying_left']-1
            reindeers[name]['dist_traveled'] = info['dist_traveled'] + info['speed']
            if info['flying_left'] == 0 and info['resting_left'] == 0:
                reindeers[name]['resting_left'] = info['rest_time']
        elif info['resting_left'] > 0:
            reindeers[name]['resting_left'] = info['resting_left']-1
            if info['resting_left'] == 0:
                reindeers[name]['flying_left'] = info['flying_time']

print("The winning reindeer has traveled", max(map(lambda x : reindeers[str(x)]['dist_traveled'], reindeers)), "km")