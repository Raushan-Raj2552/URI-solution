a,b,c,d = map(int,input().split())
e = max(a,b,c)
f = max(b,c,d)
g = max(c,d,a)
h = max(d,a,b)
if (a+b+c-2*e)>0 :
    print('S')
elif (b+c+d-2*f)>0 :
    print('S')
elif (a+c+d-2*g)>0 :
    print('S')
elif (a+b+d-2*h)>0 :
    print('S')
else:
    print('N')