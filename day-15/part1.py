#!/usr/local/bin/python3

data_file = './data.txt'
# data_file = './data-example.txt'


BOLD = '\033[1m'
END = '\033[0m'

m = []
with open(data_file) as f:
    line = f.readline()
    while line:
        m.append([int(x) for x in line.strip()])
        line = f.readline()

dirs = [(0, 1), (1, 0), (-1, 0)]
# dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = set()

def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print()

def print_path(m, path):

    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ') if (i, j) not in path else print(f"{BOLD}{m[i][j]}{END}", end=' ')
        print()

scores = []
l_rows = len(m)
l_cols = len(m[0])
pathes = {}
visited = {}
def advance(pos, prev, visited):
    if pos in visited:
        return visited[pos][0], visited[pos][1]
    if pos == (l_rows - 1, l_cols - 1):
        return [pos], m[l_rows - 1][l_cols - 1]
    
    sub_pathes = {}
    for d in dirs:
        next = (d[0] + pos[0], d[1] + pos[1])
        if prev != next and 0 <= next[0] < l_rows and 0 <= next[1] < l_cols:
            p = (pos[0] + d[0], pos[1] + d[1])
            # print(p, prev, next)
            sub_path, score = advance(p, pos, visited)
            if len(sub_path) > 0:
                sub_pathes[score] = sub_path

    min_score = min([x for x in sub_pathes.keys()])
    path = [pos]
    path.extend(sub_pathes[min_score])
    score =  min_score + m[pos[0]][pos[1]] if pos != (0, 0) else min_score
    visited[pos] = [path, score]
    return path, score



print_m(m)

path, score = advance((0, 0), (0, 0), visited)
print_path(m, path)
print(score)
print(len(visited))