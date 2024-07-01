for i in range(5,52,2):
    pattern=(i*0.1)
    print(round(pattern,1),"^2",end="")
    if i!=51:
        print(",",end="")