#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'
# data_file = Path(__file__).parent.absolute() / 'data-example.txt'

with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    bits = [0] * len(line)
    while line:
        for pos in range(0, len(line)):
            bits[pos] = bits[pos] + (1 if line[pos] == '1' else -1)
        line = fd.readline().strip()

gamma_bin   = ''.join(['1' if x > 0 else '0' for x in bits])
epsilon_bin = ''.join(['1' if x < 0 else '0' for x in bits])
gamma       = int(gamma_bin, 2)
epsilon     = int(epsilon_bin, 2)

print(bits)
print(f"Gamma bin : {gamma_bin} | Epsilon bin : {epsilon_bin}")
print(f"Gamma : {gamma} | Epsilon : {epsilon} | Gamma * Epsilon : {gamma * epsilon}")