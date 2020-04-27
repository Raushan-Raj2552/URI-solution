a = int(input())
for i in range(a):
    b,c,d,e = input().split()
    m,n = map(int,input().split())
    o = m+n
    if o%2==0:
        if c=='PAR':
            print(b)
        elif e=='PAR':
            print(d)
    else:
        if c=='IMPAR':
            print(b)
        elif e=='IMPAR':
            print(d)