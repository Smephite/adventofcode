import sys, os
sys.path.append(os.path.abspath("."))
import aoc

def next_pwd(old_pwd):
    chars = list(reversed(old_pwd))

    chars[0] = chr(ord(chars[0])+1)

    for i in range(len(chars)):
        if ord(chars[i]) > ord('z'):
            chars[i] = 'a'
            if len(chars)-1 != i:
                chars[i+1] = chr(ord(chars[i+1])+1)
    
    chars.reverse()
    

    reset = False
    for i in range(len(chars)):
        if reset:
            chars[i] = 'a'
        else:
            reset = chars[i] in ['i', 'l', 'o']
            if reset:
                chars[i] = chr(ord(chars[i])+1)

    return "".join(chars)

def check_pwd(pwd):
    straight = False
    for i in range(0, len(pwd)-2):
        chr_1 = ord(pwd[i])
        chr_2 = ord(pwd[i+1])
        chr_3 = ord(pwd[i+2])
        if chr_1 == chr_2-1 and chr_2 == chr_3-1:
            straight = True
            break
    only_allowed_chrs = not any(filter(lambda x : x in ['i','o', 'l'], list(pwd)))
    
    pairs = 0
    pair_chars = []

    for i in range(0, len(pwd)-1):
        pair = pwd[i] == pwd[i+1] and pwd[i] not in pair_chars
        if i != len(pwd)-2:
            pair = pair and pwd[i] != pwd[i+2]
        if pair:
            pair_chars.append(pwd[i])
            pairs += 1

    contains_pair = pairs >= 2


    return straight and only_allowed_chrs and contains_pair

def generate_next(old_pwd):
    pwd = next_pwd(old_pwd)
    while not check_pwd(pwd):
        pwd = next_pwd(pwd)
    return pwd


pwd = aoc.aoc()[0]


print("next after next pwd is", generate_next(generate_next(pwd)))