# program to print the power set of the input set

from itertools import combinations

def print_powerset(string):
    if len(string) == 0:
        print()
    else:
        for i in range(0, len(string)+1):
            for element in combinations(string, i):
                print(' '.join(element))

try:
    inp = input()
    print_powerset(inp.replace(" ", ""))
except:
    pass