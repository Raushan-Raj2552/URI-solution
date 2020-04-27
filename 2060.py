while True:
    n,m = map(int,input().split())
    a = 0
    if n==0 and m==0:
        break
    else:
        c = input().split()
        for i in c:
            if i.count>1:
                a+=1
    print(a)