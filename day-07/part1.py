#!/usr/local/bin/python3

from pathlib import Path
import numpy as np
from time import time

start = time()

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

with open(data_file, 'r') as fd:
    crabs = [int(x) for x in fd.readline().strip().split(',')]

maxi = max(crabs)
positions = [0] * (maxi + 1)
for crab in crabs:
    positions[crab] += 1

destinations = [0] * (maxi + 1)
for d in range(0, len(destinations)):
    for p in range(0, len(positions)):
        destinations[d] += positions[p] * abs(d - p)

print(min(destinations))

print(f"It took {time() - start} seconds")