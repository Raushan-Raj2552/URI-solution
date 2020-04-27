while True:
    try:
        a = int(input())
        if a == 0:
            break
        else:
            b = input().split()
            c = 0
            d = 0
            for i in b:
                if i=='0':
                    c+=1
                elif i=='1':
                    d+=1
            if c>d:
                print('Y')
            else:
                print('N')
    except EOFError:
        break