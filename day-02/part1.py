#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'

x = 0
y = 0
with open(data_file, 'r') as fd:
    line = fd.readline()
    while line:
        (cmd, val) = line.split(' ')
        if (cmd == 'forward'): x += int(val)
        if (cmd == 'down'): y += int(val)
        if (cmd == 'up'): y -= int(val)
        line = fd.readline()

print(f"x = {x} - y = {y} - x*y = {x * y}")
