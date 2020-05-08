while True:
    try:
        a,b,c = input().split()
        if a==b==c:
            print("*")
        elif a==b:
            print("C")
        elif b==c:
            print("A")
        elif c==a:
            print("B")
    except EOFError:
        break