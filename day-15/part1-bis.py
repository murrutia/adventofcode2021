#!/usr/local/bin/python3

class Cell:
    x = 0
    y = 0
    distance = 0

    def __init__ (self, x, y, distance):
        self.row = x
        self.col = y
        self.distance = distance

    def __lt__ (self, other):
        if (self.distance == other.distance):
            if (self.x != other.x):
                return self.x < other.x
            return self.y < other.y
        return self.distance < other.distance

    def __str__ (self):
        return "(" + str(self.row) + ", " + str(self.col) + ") d: " + str(self.distance)

    def __repr__ (self):
        return self.__str__()

def isInsideGrid (i, j, row, col):
    return i >= 0 and i < row and j >= 0 and j < col

def get_path(dis):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    pos = (len(dis) - 1, len(dis[0]) -1)
    path = [pos]
    visited = set()
    while pos != (0, 0):
        scores = {}
        for i in range(4):
            next = (pos[0] + dx[i], pos[1] + dy[i])
            if next not in visited and 0 <= next[0] < len(dis) and 0 <= next[1] < len(dis[0]):
                score = dis[pos[0]][pos[1]]
                scores[score] = next
                visited.add(next)
        print(scores)
        pos = scores[min(scores.keys())]
        path.append(pos)

    return path


def print_path(m, path):

    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ') if (i, j) not in path else print(f"{BOLD}{m[i][j]}{END}", end=' ')
        print()

def shortest (grid):
    dis = [[9999999999 for j in grid[0]] for i in grid]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    st = []
    st.append(Cell(0, 0, 0))

    dis[0][0] = 0

    while (len(st) != 0):
        k = st[0]
        st.pop(0)

        for i in range(4):
            x = k.row + dx[i]
            y = k.col + dy[i]

            if (not isInsideGrid(x, y, len(grid[0]), len(grid))):
                continue

            if (dis[x][y] > dis[k.row][k.col] + grid[x][y]):
                if (dis[x][y] != 9999999999 and Cell(x, y, dis[x][y]) in st):
                    st.pop(st.index(Cell(x, y, dis[x][y])))

                dis[x][y] = dis[k.row][k.col] + grid[x][y]
                st.append(Cell(x, y, dis[x][y]))

    print_path(grid, get_path(dis))
    return dis[-1][-1]

inputFile = open("data.txt", "r")
chitons = []

for line in inputFile:
    chitons.append([int(x) for x in line.strip()])

risk = shortest(chitons)
print("Shortest path:", risk)