for i in range(27):
    for j in range(ord("A"), ord("Z")+1):
        x = chr(j)
        y = str(x) + ".txt"
        i = open(y, "i")