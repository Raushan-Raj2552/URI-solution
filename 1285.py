while True:
    try:
        a,b = map(int,input().split())
        c = 0
        for i in range(a,b+1):
            if len(str(i))==len(set(str(i))):
                c+=1
        print(c)
    except EOFError:
        break