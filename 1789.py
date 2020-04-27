while True:
    try:
        a = 0
        l = int(input())
        v = input().split()
        for i in range(l):
            if int(v[i]) > a:
                a = int(v[i])

        if a < 10:
            level = 1
        elif a >= 10 and a < 20:
            level = 2
        else:
            level =3
        print(level)

    except EOFError:
        break