while True:
    try:
        a = int(input())
        b = []
        for i in range(a):
            c = str(input())
            b.append(c)
        b.sort()
        for j in b:
            print(j)
    except EOFError:
        break