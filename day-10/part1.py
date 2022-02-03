#!/usr/local/bin/python3

from pathlib import Path
from collections import deque

data_file = Path(__file__).absolute().parent / 'data.txt'
data_file = Path(__file__).absolute().parent / 'data-example.txt'

couples = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def check_not_corrupted(line):
    openers = deque()
    for x in line:
        if x in points:
            if len(openers) == 0 or openers[-1] != couples[x]:
                return False
    return True


lines = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        if check_not_corrupted(line):
            lines.append(line)
            print(line)
        line = fd.readline().strip()

print(lines)