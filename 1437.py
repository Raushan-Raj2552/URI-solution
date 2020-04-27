while True:
    a = int(input())
    if a == 0:
        break
    else:
        b = input()
        c = b.count('D')
        d = b.count('E')
        if (c-d)%4==0:
            print('N')
        elif (c-d)%4==1:
            print('L')
        elif (c-d)%4==2:
            print('S')
        elif (c-d)%4==3:
            print('O')