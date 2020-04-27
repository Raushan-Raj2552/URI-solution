while True:
    a = int(input())
    if a == 0 :
        break
    if a > 0 :
        x,y = map(int,input().split())
        for i in range(a):
            b,c = map(int,input().split())
            if (b-x)==0 or (c-y)==0 :
                print('divisa')
            if (b-x)>0 and (c-y)>0 :
                print('NE')
            if (b-x)<0 and (c-y)>0 :
                print('NO')
            if (b-x)>0 and (c-y)<0 :
                print('SE')
            if (b-x)<0 and (c-y)<0 :
                print('SO')