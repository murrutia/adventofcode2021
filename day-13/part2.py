#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'
# data_file = Path(__file__).parent.absolute() / 'data-example.txt'

dots = set()
folds = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        dot = [int(x) for x in line.split(',')]
        dots.add((dot[0], dot[1]))
        line = fd.readline().strip()
    
    print('folds')
    
    line = fd.readline().strip()
    while line:
        axis, pos = line.split(' ')[2].split('=')
        folds.append((axis, int(pos)))
        line = fd.readline().strip()


def apply_fold(dots, fold):
    to_remove = set()
    to_add = set()
    if fold[0] == 'x':
        x = fold[1]
        for dot in dots:
            if dot[0] > x:
                to_remove.add(dot)
                to_add.add((x - (dot[0] - x), dot[1]))

    else:
        y = fold[1]
        for dot in dots:
            if dot[1] > y:
                to_remove.add(dot)
                to_add.add((dot[0], y - (dot[1] - y)))
    
    for dot in to_remove:
        dots.remove(dot)
    for dot in to_add:
        dots.add(dot)

for f in folds:
    apply_fold(dots, f)

max_x, max_y = 0, 0
for dot in dots:
    max_x = dot[0] if dot[0] > max_x else max_x
    max_y = dot[1] if dot[1] > max_y else max_y

for y in range(max_y+1):
    for x in range(max_x+1):
        if (x, y) in dots:
            print('#', end='')
        else:
            print('.', end='')
    print()