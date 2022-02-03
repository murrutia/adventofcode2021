#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'


def check_low_points(lines, j, low_points):
    l = len(lines[0])
    ll = len(lines)
    for i in range(0, len(lines[0])):
        cur = lines[j][i]
        lower = True
        
        if i > 0:
            lower = cur < lines[j][i-1]
        if lower and j > 0:
            lower = cur < lines[j-1][i]
        if lower and i < l-1:
            lower = cur < lines[j][i+1]
        if lower and j < ll-1:
            lower = cur < lines[j+1][i]
        
        if lower:
            low_points.append(int(cur) + 1)


low_points = []
lines = [''] * 3

with open(data_file, 'r') as fd:
    lines[0] = fd.readline().strip()
    lines[1] = fd.readline().strip()
    lines[2] = fd.readline().strip()

    check_low_points(lines, 0, low_points)
    check_low_points(lines, 1, low_points)
    lines.pop(0)

    line = fd.readline().strip()
    while line:
        lines.append(line)
        check_low_points(lines, 1, low_points)
        lines.pop(0)
        line = fd.readline().strip()

    check_low_points(lines, 1, low_points)

print(sum(low_points), low_points)
