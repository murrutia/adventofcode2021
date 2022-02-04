#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
data_file = Path(__file__).absolute().parent / 'data-example.txt'

octopuses = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        octopuses.append([int(x) for x in line])
        line = fd.readline().strip()

def  display_octopuses(octopuses):
    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            print(octopuses[r][c], end=" ")
        print()

def step_up(r, c, octopuses, flashed):
    octopuses[r][c] += 1


steps = 1
total_flashed = 0
for i in range(steps):
    flashed = set()
    for r in range(len(octopuses)):
        for c in range(len(octopuses[0])):
            step_up(r, c, octopuses, flashed)
    total_flashed += len(flashed)

display_octopuses(octopuses)
# print(total_flashed)