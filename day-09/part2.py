#!/usr/local/bin/python3

from math import prod
from pathlib import Path
from collections import deque


data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'


data = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        data.append([int(x) for x in line])
        line = fd.readline().strip()

def discover_point(row, col, data, visited):

    row_count = len(data)
    col_count = len(data[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    to_visit = deque(((row, col),))
    ret = set()

    while to_visit:
        r, c = to_visit.popleft()
        visited.add((r, c))
        if data[r][c] < 9:
            ret.add((r, c))
            for dir in range(len(directions)):
                dir_row = directions[dir][0]
                dir_col = directions[dir][1]
                if 0 <= r + dir_row < row_count and 0 <= c + dir_col < col_count:
                    if (r + dir_row, c + dir_col) not in visited:
                        visited.add((r + dir_row, c + dir_col))
                        to_visit.append((r + dir_row, c + dir_col))
        
    return (len(ret), ret)

def get_largest_basins(data):
    basins_size = []
    visited = set()
    for row in range(len(data)):
        for col in range(len(data[row])):
            if (row, col) not in visited:
                basins_size.append(discover_point(row, col, data, visited))

    return sorted(basins_size)[-3:]

largest_basins = [x[0] for x in get_largest_basins(data)]
print(largest_basins)
print(prod(largest_basins))