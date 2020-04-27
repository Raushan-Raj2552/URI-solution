a0,b0,c0,d0,e0 = map(int,input().split())
a1,b1,c1,d1,e1 = map(int,input().split())
if a0 + a1 == 1:
    if b0 + b1 == 1:
        if c0 + c1 == 1:
            if d0 + d1 == 1:
                if e0 + e1 == 1:
                    print('Y')
                else:
                    print('N')
            else:
                print('N')
        else:
            print('N')
    else:
        print('N')
else:
    print('N')
    
    