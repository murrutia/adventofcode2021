#!/usr/local/bin/python3

import re
from time import time
from pathlib import Path

start = time()

data_file = Path(__file__).parent.absolute() / 'data.txt'
data_file = Path(__file__).parent.absolute() / 'data-example.txt'

rules = []
with open(data_file, 'r') as fd:
    template = fd.readline().strip()
    
    fd.readline().strip()
    line = fd.readline().strip()
    while line:
        pair, letter = line.split(' -> ')
        rules.append((pair, letter))
        line = fd.readline().strip()


def add_letters(string, to_insert, current_index):
    s = ''
    string = list(string)
    letters = list(to_insert.values())
    indexes = list(to_insert.keys())
    while len(letters) > 0:
        letter = letters.pop()
        index = indexes.pop()
        while index != current_index:
            s += string.pop(0)
            current_index += 1

        s += letter
    
    s += ''.join(string)
    return s


def sort_dict(dict):
    keys = sorted(dict.keys(), reverse=True)
    d = {}
    for k in keys:
        d[k] = dict[k]
    return d

steps = 20

for step in range(steps):
    found = {}
    for rule in rules:
        for m in re.finditer(f'(?={rule[0]})', template):
            found[m.start() + 1] = rule[1]
    found = sort_dict(found)
    three = time()

    template = add_letters(template, found, 0)
    

letters = {}
for x in template:
    if x not in letters:
        letters[x] = 0
    letters[x] += 1

# print(letters)
scores = sorted([letters[x] for x in letters])
# print(template)
print(scores[-1] - scores[0])
# print(rules)
print(time() - start)