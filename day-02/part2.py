#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'

x = 0
y = 0
aim = 0
with open(data_file, 'r') as fd:
    line = fd.readline()
    while line:
        (cmd, val) = line.split(' ')
        if (cmd == 'forward'):
            xx = int(val)
            print(f"x += {xx} | aim = {aim} | y += {xx * aim}")
            x += xx
            y += xx * aim
        if (cmd == 'down'): 
            aim += int(val)
            print(f"aim += {int(val)} | aim = {aim}")
        if (cmd == 'up'):
            aim -= int(val)
            print(f"aim -= {int(val)} | aim = {aim}")
        line = fd.readline()

print(f"x = {x} | y = {y} | aim = {aim} | x*y = {x * y}")
