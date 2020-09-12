try:
    inp = input()
    if len(inp) == 0:
        for i in range(3):
            print()
    else:
        for i in range(3):
            print(inp)
except EOFError:
    pass
