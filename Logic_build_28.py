for i in range(1, 26):
    if i % 2 != 0 and i % 5 != 0:
        print(i, end=",")
    elif i % 5 == 0:
        print("Divisible by 5", end="")
        if i != 25:
            print(",", end="")
