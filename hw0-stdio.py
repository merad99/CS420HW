try:
    inp = input()
    if inp == "":
        print()
    else:
       for i in range(3):
            print(inp)
except EOFError:
    pass


