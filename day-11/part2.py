#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

octopuses = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        octopuses.append([int(x) for x in line])
        line = fd.readline().strip()

def  display_octopuses(octopuses):
    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            o = octopuses[r][c]
            if o == 0:
                print(f"{color.BOLD}0{color.END}", end=" ")
            else:
                print(octopuses[r][c], end=" ")
        print()

def step_up(r, c, octopuses, flashed):
    if 0 <= r < len(octopuses) and 0 <= c < len(octopuses[0]) and (r, c) not in flashed:
        octopuses[r][c] += 1
        if octopuses[r][c] > 9:
            flashed.add((r, c))
            octopuses[r][c] = 0
            for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                step_up(r+d[0], c+d[1], octopuses, flashed)



display_octopuses(octopuses)
print()

steps = 0
total_flashed = 0
all = len(octopuses) * len(octopuses[0])

while True:
    steps += 1
    flashed = set()
    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            step_up(r, c, octopuses, flashed)
    total_flashed += len(flashed)
    
    display_octopuses(octopuses)
    print()

    if len(flashed) == all:
        break



print(steps)