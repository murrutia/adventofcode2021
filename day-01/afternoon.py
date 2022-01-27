#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'

values = []
increased = 0
with open(data_file, 'r') as fd:
    line = fd.readline()
    while line:
        values.append(line)
        if len(values) == 4:
            left = int(values[0]) + int(values[1]) + int(values[2])
            right = int(values[1]) + int(values[2]) + int(values[3])
            print(f"Left : {left} - Right : {right}")
            if left < right:
                increased += 1
            values.pop(0)

        line = fd.readline()

print(f"The values increased {increased} times")
