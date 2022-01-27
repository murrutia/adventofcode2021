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

def draw_board(board):
    for y in range(0, 5):
        for x in range(0, 5):
            if board[y][x][1] is True:
                print(f"{color.BOLD}{board[y][x][0]: >2d}{color.END}", end=' ')
            else:
                print(f"{board[y][x][0]: >2d}", end=' ')
        print()


def check_number(board, n):
    y = 0
    found = False
    while y < 5 and not found:
        x = 0
        while x < 5 and not found:
            found = board[y][x][0] == n
            if found: board[y][x][1] = True
            else: x += 1
        if not found: y += 1
    return (found, x, y)


def check_line(board, y):
    checked = [cell[1] for cell in board[y]]
    return not False in checked


def check_column(board, x):
    checked = [line[x][1] for line in board]
    return not False in checked


def check_board(board, x, y):
    winner = check_line(board, y)
    if not winner:
        winner = check_column(board, x)
    return winner

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
        
        boards.append(board)
        line = fd.readline()
    
winner = False
n = 0
while n < len(numbers) and not winner:
    number = numbers[n]
    print(f"number : {number}")
    b = 0
    while b < len(boards) and not winner:
        board = boards[b]
        (found, x, y) = check_number(board, number)
        print()
        draw_board(board)
        print(found, x, y)
        if found:
            winner = check_board(board, x, y)
        b += 1
    n += 1

if winner:
    unchecked = []
    for y in range(0, 5):
        line_unchecked = [x[0] for x in board[y] if not x[1]]
        unchecked.extend(line_unchecked)
    
    print(number * sum(unchecked))
