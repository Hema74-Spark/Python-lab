num = int(input())
if 0 < num < 100:
    if 90 <= num < 100:
        print("Super Smart")
    elif 80 <= num < 90:
        print("smart")
    elif 70 <= num < 80:
        print("smart enough")
    elif 60 <= num < 70:
        print("Just Smart")
    elif 35 <= num < 60:
        print("No Smart")
    elif 0 <= num < 35:
        print("Dump")
else:
    print("invalid input")
