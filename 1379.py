while True:
    a,b = map(int,input().split())
    if a == 0  and b == 0:
        break
    if a > 0  and b>0:
        print(2*a-b)