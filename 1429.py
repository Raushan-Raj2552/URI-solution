while True:
    a = str(input())
    if int(a) == 0:
        break
    elif len(a) == 5:
        print((int(a[0])*5*4*3*2)+(int(a[1])*4*3*2)+(int(a[2])*3*2)+(int(a[3])*2)+(int(a[4])))
    elif len(a) == 4:
        print((int(a[0])*4*3*2)+(int(a[1])*3*2)+(int(a[2])*2)+(int(a[3])))
    elif len(a) == 3:
        print((int(a[0])*3*2)+(int(a[1])*2)+(int(a[2])))
    elif len(a) == 2:
        print((int(a[0])*2)+(int(a[1])))
    elif len(a) == 1:
        print(int(a[0]))