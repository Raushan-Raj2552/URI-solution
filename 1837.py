import math as m
a,b = map(int,input().split())
if a>=0 and b>0:
    c = (a//b)
    d = (a%b)
    print(c,d)
elif a>=0 and b<0:
    c = m.ceil(a/b)
    d = a-(b*c)
    print(c,d)
elif a<=0 and b>0:
    c = (a//b)
    d = a%abs(b)
    print(c,d)
elif a<=0 and b<0:
    c = m.ceil(abs(a)/abs(b))
    d = a-(b*c)
    print(c,d)