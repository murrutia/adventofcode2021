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
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def score_incomplete(line):
    openers = deque()
    score = 0
    for x in line:
        if x in couples:
            if len(openers) == 0 or openers[-1] != couples[x]:
                return 0
            else:
                openers.pop()
        else:
            openers.append(x)

    while len(openers) > 0:
        x = openers.pop()
        score = score * 5 + points[x]
    
    return score


scores = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        s = score_incomplete(line)
        if s != 0:
            scores.append(s)
        line = fd.readline().strip()
scores = sorted(scores)
print(scores)
print(scores[len(scores) // 2])