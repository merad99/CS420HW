import sys
try:
    msg = sys.stdin.readlines()
    for item in msg:
        for i in range(3):
            print(item)
except:
    pass
