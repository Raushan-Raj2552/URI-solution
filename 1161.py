while True:
    try:
        a,b = map(int,input().split())
        c = 1
        d = 1
        for i in range(1,a+1):
            c*=i
        for j in range(1,b+1):
            d*=j
        print(c+d)
    except EOFError:
        break