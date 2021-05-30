from itertools import dropwhile

with open('test.txt') as f:
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line, end='')