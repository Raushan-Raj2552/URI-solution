a = int(input())
e = 0
f = 0
for i in range(a):
    b = float(input())
    f+=b
    c = str(input())
    d = c.count(' ')
    e+=(d+1)
    print('day '+str(i+1)+':',(d+1),'kg')
print('%0.2f'%(e/a),'kg by day')
print('R$','%0.2f'%(f/a),'by day')