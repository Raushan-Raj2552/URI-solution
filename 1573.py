while True:
    a,b,c = map(int,input().split())
    if a == 0  and b == 0 and c == 0:
        break
    if a > 0  and b>0 and c>0 :
        d = (a*b*c)**(1/3)
        e = d//1
        print('%0.0f'%(e))