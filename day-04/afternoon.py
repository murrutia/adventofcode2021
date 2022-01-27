#!/usr/local/bin/python3

import re
from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Board:
    def __init__(self, board):
        self.board = board
        self.winner = False
    
    def draw(self):
        for y in range(0, 5):
            for x in range(0, 5):
                if self.board[y][x][1] is True:
                    print(f"{color.BOLD}{self.board[y][x][0]: >2d}{color.END}", end=' ')
                else:
                    print(f"{self.board[y][x][0]: >2d}", end=' ')
            print()
        print(f"Winner : {self.winner}")

    def check_number(self, n):
        y = 0
        found = False
        while y < 5 and not found:
            x = 0
            while x < 5 and not found:
                found = self.board[y][x][0] == n
                if found: self.board[y][x][1] = True
                else: x += 1
            if not found: y += 1
        return (found, x, y)

    def check_line(self, y):
        checked = [cell[1] for cell in self.board[y]]
        return not False in checked

    def check_column(self, x):
        checked = [line[x][1] for line in self.board]
        return not False in checked

    def check(self, x, y):
        self.winner = self.check_line(y)
        if not self.winner:
            self.winner = self.check_column(x)
        return self.winner


with open(data_file, 'r') as fd:
    numbers = [int(x) for x in fd.readline().strip().split(',')]
    
    boards = []
    line = fd.readline() # blank line

    while line:
        board = []
        for i in range(0, 5):
            line = fd.readline().strip()
            line_trimmed = re.sub(r'[ ]+', ' ', line)
            board.append([[int(x), False] for x in line_trimmed.split(' ')])
        
        boards.append(Board(board))
        line = fd.readline()
    
winner = False
n = 0
while n < len(numbers) and len(boards) > 0:
    number = numbers[n]
    print(f"\nnumber : {number}")
    b = 0
    for b in range(0, len(boards)):
        board = boards[b]
        (found, x, y) = board.check_number(number)
        if found:
            print()
            board.draw()
            if board.check(x, y):
                winner = True
    n += 1
    if winner:
        for i in range(0, len(boards)):
            print()
            boards[i].draw()
        boards = [b for b in boards if not b.winner]
        winner = False

unchecked = []
for y in range(0, 5):
    line_unchecked = [x[0] for x in board.board[y] if not x[1]]
    unchecked.extend(line_unchecked)

print(number * sum(unchecked))
