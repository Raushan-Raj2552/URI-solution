while True:
    a = int(input())
    if a == 0 :
        break
    if a !=0 :
        b = 0
        c = 0
        for i in range(a):
            d,e = map(int,input().split())
            if d>e:
                b+=1
            elif(d<e):
                c+=1
        print(b,c)