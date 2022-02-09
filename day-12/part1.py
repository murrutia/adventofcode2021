#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).parent.absolute() / 'data.txt'
# data_file = Path(__file__).parent.absolute() / 'data-example.txt'
# data_file = Path(__file__).parent.absolute() / 'data-example2.txt'
# data_file = Path(__file__).parent.absolute() / 'data-example3.txt'


connections = {}
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        a, b = line.split('-')
        
        if a != 'end' and b != 'start':
            if a not in connections:
                connections[a] = []
            connections[a].append(b)

        if b != 'end' and a != 'start':
            if b not in connections:
                connections[b] = []
            connections[b].append(a)
            
        line = fd.readline().strip()


print(connections)

def follow_path(connections, visited, part, path):
    path = f"{path},{part}" if path != '' else 'start'
    if part not in ['start', 'end'] and part.islower():
        if part in visited:
            return []
        else:
            visited.append(part)

    if part == 'end':
        return [ path ]
    
    paths = []
    for p in connections[part]:
        found = follow_path(connections, visited[:], p, path)
        paths.extend(found)
    
    return paths

paths = follow_path(connections, [], 'start', '')
for p in paths:
    print(p)

print(len(paths))

