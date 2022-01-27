#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'

prev = None
increased = 0
with open(data_file, 'r') as fd:
    line = fd.readline()
    while line:
        print(line)
        if prev is not None and line > prev:
            increased += 1
        prev = line
        line = fd.readline()

print(f"The values increased {increased} times")
