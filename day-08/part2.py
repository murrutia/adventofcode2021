#!/usr/local/bin/python3

from pathlib import Path

data_file = Path(__file__).absolute().parent / 'data.txt'
# data_file = Path(__file__).absolute().parent / 'data-example.txt'

easy_nums = { 
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

inputs = []
with open(data_file, 'r') as fd:
    line = fd.readline().strip()
    while line:
        parts = line.split('|')
        segments = [''.join(sorted(x)) for x in parts[0].strip().split(' ')]
        segments = sorted(segments, key=lambda x: len(x))

        digits = [''.join(sorted(x)) for x in parts[1].strip().split(' ')]
        
        inputs.append({ "segments": segments, "digits": digits})
        
        line = fd.readline().strip()

def get_wiring(segments):
    # segments dans 1
    cf = segments[0]

    # segment manquant entre 1 et 7
    a = ''.join([x for x in cf if x not in segments[1]])

    # segments de 4 manquant dans 1
    bd = [x for x in segments[2] if x not in segments[0]]

    # segments de 8 manquant dans 4 et n'étant pas 'a'
    eg = [x for x in segments[9] if x not in segments[2] and x != a]
    
    # segments de 8 manquant dans 0, 6 et 9
    cde = [x for x in segments[9] if x not in segments[6] or x not in segments[7] or x not in segments[8]]

    # croisement de cf / cde pour trouver c et déduire f
    c = ''.join([x for x in cf if x in cde])
    f = ''.join([x for x in cf if x != c])

    # croisement eg / cde pour trouver e et déduire g
    e = ''.join([x for x in eg if x in cde])
    g = ''.join([x for x in eg if x != e])

    # déduction de d dans cde
    d = ''.join([x for x in cde if x != c and x != e])
    # déduction de b dans bd
    b = ''.join([x for x in bd if x != d])

    # a, b, c, d, e, f, g
    return {
        ''.join(sorted(a + b + c + e + f + g)): 0,
        segments[0]: 1,
        ''.join(sorted(a + c + d + e + g)): 2,
        ''.join(sorted(a + c + d + f + g)): 3,
        segments[2]: 4,
        ''.join(sorted(a + b + d + f + g)): 5,
        ''.join(sorted(a + b + d + e + f + g)): 6,
        segments[1]: 7,
        segments[9]: 8,
        ''.join(sorted(a + b + c + d + f + g)): 9
    }

appearances = [0] * 10
numbers = []
for line in inputs:
    wiring = get_wiring(line['segments'])
    number = 0
    for digit in line['digits']:
        appearances[wiring[digit]] += 1
        number = number * 10 + wiring[digit]

    numbers.append(number)
    print(number)

for i in range(0, 10):
    print(f"The digit {i} appears {appearances[i]} times")

print(sum(appearances), sum(numbers))
