
# program to print the power set of the input set

from itertools import combinations


def print_powerset(set):
    for i in range(0, len(set)+1):
        for element in combinations(set, i):
            print(' '.join(element))


try:
    inp = input()
    print_powerset(inp.replace(" ", ""))
except:
    pass
