for i in range(2, 17):
    next_number = i + 1
    print(i, "*", next_number, end="")
    if i != 16:
        print(end=",")
print()
for i in range(2, 17):
    next_number = i + 1
    print(i * next_number, end="")
    if i != 16:
        print(end=",")
