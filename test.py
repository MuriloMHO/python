def printA(x):
    print("A")
    if x >= 5:
        return
    else:
        printA(x+1)

printA(1)