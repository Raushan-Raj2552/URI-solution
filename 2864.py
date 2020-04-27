a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    e = (4*b*d)-(c*c)
    f = 4*b
    print('%0.2f'%(e/f))