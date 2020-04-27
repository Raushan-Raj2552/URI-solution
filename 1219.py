while True:
    try:
        import math as m
        a,b,c = map(int,input().split())
        s = (a+b+c)/2
        d = (a+b+c)*(b+c-a)*(a-b+c)*(a+b-c)
        e = ((s-a)*(s-b)*(s-c))/s
        R = (a*b*c)/(m.sqrt(d))
        r = m.sqrt(e)
        AC = m.pi*(R*R)
        AT = r*s
        Ac = m.pi*(r*r)
        print('%0.4f'%(AC-AT),'%0.4f'%(AT-Ac),'%0.4f'%(Ac))
    except EOFError:
        break