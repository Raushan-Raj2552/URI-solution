while True:
    try:
        a = int(input())
        if 1000<a<10000:
            print(a-1)
    except EOFError:
        break