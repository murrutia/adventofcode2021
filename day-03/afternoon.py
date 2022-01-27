#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

with open(data_file, 'r') as fd:
    lines = fd.read().split('\n')

pos = 0
l = len(lines[0])
oxygen_lines = lines
while pos < l and len(oxygen_lines) > 1:
    bit = 0
    for i in range(0, len(oxygen_lines)):
        bit += 1 if oxygen_lines[i][pos] == '1' else -1
    bit = '1' if bit >= 0 else '0'
    oxygen_lines = [line for line in oxygen_lines if line[pos] == bit]
    pos += 1

oxygen = int(oxygen_lines[0], 2)
print(oxygen_lines, oxygen)

pos = 0
l = len(lines[0])
co2_lines = lines
while pos < l and len(co2_lines) > 1:
    bit = 0
    for i in range(0, len(co2_lines)):
        bit += 1 if co2_lines[i][pos] == '1' else -1
    bit = '0' if bit >= 0 else '1'
    co2_lines = [line for line in co2_lines if line[pos] == bit]
    pos += 1

co2 = int(co2_lines[0], 2)
print(co2_lines, co2)

print(oxygen * co2)