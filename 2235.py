a,b,c = map(int,input().split())
if 1<=a<=1000:
    if 1<=b<=1000:
        if 1<=c<=1000:
            d = max(a,b,c)
            if a==b:
                print('S')
            elif a==c:
                print('S')
            elif b==c:
                print('S')
            elif (a+b+c-2*d)==0:
                print('S')
            else:
                print('N')