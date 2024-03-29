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

steps = 4
# print(template)
for step in range(steps):
    found = {}
    for rule in rules:
        for m in re.finditer(f'(?={rule[0]})', template):
            found[m.start() + 1] = rule[1]
    added = 0
    for i in sorted(found):
        template = template[:(i + added)] + found[i] + template[(i + added):]
        added += 1
    # print(template)
    

letters = {}
for x in template:
    if x not in letters:
        letters[x] = 0
    letters[x] += 1

# print(letters)
scores = sorted([letters[x] for x in letters])
print(scores[-1] - scores[0])
# print(rules)
print(time() - start)