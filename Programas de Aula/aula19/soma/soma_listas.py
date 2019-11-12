import sys

for caso in map(eval, sys.stdin):
    print(sum(caso))
