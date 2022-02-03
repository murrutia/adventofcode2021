#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

easy_nums = { 
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

inputs = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        parts = line.split('|')
        segments = parts[0].strip().split(' ')
        digits = parts[1].strip().split(' ')
        
        inputs.append({ "segments": segments, "digits": digits})
        
        line = fd.readline().strip()

appearances = [0] * 10
for line in inputs:
    for digit in line['digits']:
        if len(digit) in easy_nums:
            appearances[easy_nums[len(digit)]] += 1

for i in range(0, 10):
    print(f"The digit {i} appears {appearances[i]} times")

print(sum(appearances))