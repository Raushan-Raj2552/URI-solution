a,b,c = map(int,input().split())
if a>b and b>c :
    print(b)
elif c>b and b>a :
    print(b)
elif c>a and a>b :
    print(a)
elif b>a and a>c :
    print(a)
elif b>c and c>a :
    print(c)
elif c>b and a>c :
    print(c)