while True:
    l,c,r1,r2 = map(int,input().split())
    r = (r1+r2)
    if l==c==r1==r2==0:
        break
    elif min(l,c)>=max(2*r1,2*r2) and (r*r)<=((c-r)**2)+((l-r)**2):
        print('S')
    else:
        print('N')