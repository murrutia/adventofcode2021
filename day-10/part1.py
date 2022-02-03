#!/usr/local/bin/python3

from pathlib import Path
from collections import deque

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

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

def score_corrupted(line):
    openers = deque()
    for x in line:
        if x in points:
            if len(openers) == 0 or openers[-1] != couples[x]:
                print(f"illegal : {x}")
                return points[x]
            else:
                openers.pop()
        else:
            openers.append(x)
    return 0


lines = []
score = 0
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        s = score_corrupted(line)
        score += s
        line = fd.readline().strip()

print(score)