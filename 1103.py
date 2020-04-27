while True:
    a,b,c,d = input().split(" ")

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if (a + b + c + d) == 0:
        break
    
    if (a < c) and (b == d):
        print("%d" %((c-a)*60))
        continue
    
    if (a < c) and (b < d):
        print("%d" %((c-a)*60+(d-b)))
        continue
    
    if (a < c) and (b > d):
        print("%d" %((c-a)*60+(d-b)))
        continue
    
    if (a == c) and (b == d):
        print("%d" %(24*60))
        continue
    
    if (a == c) and (b < d):
        print("%d" %((d-b)))
        continue
    
    if (a == c) and (b > d):
        print("%d" %((24*60)+(d-b)))
        continue
    
    if (a > c) and (b == d):
        print("%d" %((c-a+24)*60))
        continue
    
    if (a > c) and (b < d):
        print("%d" %((c-a+24)*60+(d-b)))
        continue
    
    if (a > c) and (b > d):
        print("%d" %((c-a+24)*60+(d-b)))
        continue
    