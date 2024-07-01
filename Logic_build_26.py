for i in range(1, 36):
    if i % 2 != 0:
        print(i,end="")
        if i != 35:
            print(",",end="")
    else:
        print("Even,",end="")
