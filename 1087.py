while True:
    a,b,c,d = input().split(" ")

    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)

    if (a + b + c + d) == 0:
        break
    
    if (a == c) and (b == d):
        print("%d" %0)
        continue
    
    if (a == c) or (b == d):
        print("%d" %1)
        continue
    
    if abs( a-c ) == abs( b-d ):
        print("%d" %1)
        continue
    
    print("%d" %2)