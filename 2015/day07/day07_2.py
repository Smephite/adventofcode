import sys, os
sys.path.append(os.path.abspath("."))
import aoc


signals = {}
nots = {}
operators = []

digits = [str(i) for i in range(0, 10)]

def reset():

    for line in aoc.aoc():
        splits = line.split(" ")
        f1, f2, op, target = None, None, None, None
        if len(splits) == 5:
            [f1, op, f2, _, target] = splits
            operators.append((op, f1, f2, target))
        elif len(splits) == 4:
            #not
            [_, f1, _, target] = splits
            op = 'NOT'
            nots[f1] = target
        elif len(splits) == 3:
            #assignment
            [f1, _, target] = splits
            op = 'ASSIGN'
            

            if f1[0] in digits:
                signals[target] = int(f1)
            else:
                operators.append((op, f1, '-', target))

def iterate(args):
    [signals, nots, operators] = args

    direct_connect = list(filter(lambda gate: gate[0] == 'ASSIGN' and gate[1] in signals, operators))

    for (_, in1, _, out) in direct_connect:
        signals[out] = signals[in1]

    nots = dict(map(lambda b: (b[0], b[1]), filter(lambda not_game: not_game[1] not in signals.keys(), nots.items())))

    for (input, output) in filter(lambda x: x[0] in signals, dict(map(lambda b: (b[0], b[1]), filter(lambda not_game: not_game[0] in signals.keys(), nots.items()))).items()):
        signals[output] = ~signals[input] & 0xffff
    
    ops = list(filter(lambda op : (op[1] in signals.keys() or op[1][0] in digits) and (op[2] in signals.keys() or op[2][0] in digits) and op[3] not in signals.keys(), operators))

    for (op, in1, in2, out) in ops:

        if in1[0] in digits:
            a1 = int(in1)
        else:
            a1 = signals[in1]
        if in2[0] in digits:
            a2 = int(in2)
        else:
            a2 = signals[in2]

        if op == 'AND':
            signals[out] = a1 & a2
            pass
        elif op == 'OR':
            signals[out] = a1 | a2
            pass
        elif op == 'LSHIFT':
            signals[out] = (a1 << int(a2)) & 0xffff
            pass
        elif op == 'RSHIFT':
            signals[out] = (a1 >> int(a2)) & 0xffff

    return [signals, nots, operators]





reset()
last_n_sig = 0
while 'a' not in signals.keys():
    if last_n_sig == len(signals):
            print("Error! endless loop!")
            break
    last_n_sig = len(signals)
    
    [signals, nots, operators] = iterate([signals, nots, operators])

a = signals['a']

signals = {}
nots = {}
operators = []

reset()

signals['b'] = a

last_n_sig = 0
while 'a' not in signals.keys():
    if last_n_sig == len(signals):
            print("Error! endless loop!")
            break

    last_n_sig = len(signals)
    
    [signals, nots, operators] = iterate([signals, nots, operators])

if 'a' in signals:
    print(f"Final value for 'a': {signals['a']}")