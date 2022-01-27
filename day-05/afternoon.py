#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def __repr__(self):
        return f"{self.x},{self.y}"
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

class Line:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def __repr__(self):
        return f"{{{self.begin} -> {self.end}}}"
    
    def is_diagonal(self):
        return self.begin.x != self.end.x and self.begin.y != self.end.y
    
    def points(self):
        points = []
        if self.begin.x == self.end.x:
            a = self.begin.y
            b = self.end.y
            if a > b:
                a, b = b, a
            r = range(a, b+1)
            for y in r:
                points.append(Point(self.begin.x, y))
        
        if self.begin.y == self.end.y:
            a = self.begin.x
            b = self.end.x
            if a > b:
                a, b = b, a
            r = range(a, b+1)
            for x in r:
                points.append(Point(x, self.begin.y))
        
        if self.is_diagonal():
            x1 = self.begin.x
            x2 = self.end.x
            y1 = self.begin.y
            y2 = self.end.y
            xway = 1 if x1 < x2 else -1
            yway = 1 if y1 < y2 else -1

            x = x1
            y = y1
            while x != x2 and y != y2:
                points.append(Point(x, y))
                x += xway
                y += yway
            points.append(self.end)
        
        return points



l = Line(Point(0,9), Point(5,9))
print(l)
print(f"l is diagonal : {l.is_diagonal()}")

vents = []
with open(data_file, 'r') as fd:
    line = fd.readline()

    while line:
        coordinates = [p.split(',') for p in line.strip().split(' -> ')]
        points = [Point(p[0], p[1]) for p in coordinates]
        l = Line(points[0], points[1])

        vents.append(l)

        line = fd.readline()

points_dict = {}
for v in vents:
    for p in v.points():
        if p not in points_dict:
            points_dict[p] = 0
        points_dict[p] += 1

print(points_dict)
more_than_one = 0
for n in points_dict.values():
    if n > 1:
        more_than_one += 1

print(more_than_one)
