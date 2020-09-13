import sys
try:
    msg = sys.stdin.readlines()
    if (len(msg) == 0):
        for i in range(3):
            print()
    else:
        for item in msg:
            for i in range(3):
                print(item)
except:
    pass
