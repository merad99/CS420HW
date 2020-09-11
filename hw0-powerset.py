# program to print the power set of the input set

import math
import sys
from itertools import combinations

def print_powerset(string):
    for i in range(0, len(string)+1):
        for element in combinations(string, i):
            print(' '.join(element))

try:
    inp = input()
    print_powerset(inp.replace(" ", ""))
except EOFError:
    pass