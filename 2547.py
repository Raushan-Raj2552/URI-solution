while True:
    try:
        a,b,c = map(int,input().split())
        d = []
        for k in range(a):
            e = int(input())
            if b<=e<=c:
                d.append(k)
        print(len(d))
    except EOFError:
        break