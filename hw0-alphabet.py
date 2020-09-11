# program to print all possible strings of length k using recursive method

import sys

def printAll(set, k):

    n = len(set)
    printAllRec(set, "", n, k)

def printAllRec(set, prefix, n, k):

    # Base case: k is 0,
    if (k == 0):
        print(prefix)
        return

    # call for k equals to k-1
    for i in range(n):

        # Next character of input added
        newPrefix = prefix + set[i]

        # k is decreased
        printAllRec(set, newPrefix, n, k - 1)

try:
    inp = input()
    printAll(inp.replace(" ", ""), 3)
except:
    pass