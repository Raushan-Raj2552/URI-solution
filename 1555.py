a = int(input())
for i in range(a):
    x,y = map(int,input().split())
    r = (9*(x**2))+y**2
    b = (2*(x**2))+(25*(y**2))
    c = (-100*x)+(y**3)
    d = max(r,b,c)
    if d==r:
        print('Rafael ganhou')
    elif d==b:
        print('Beto ganhou')
    elif d==c:
        print('Carlos ganhou')