a = int(input())
for i in range(a):
    b = str(input())
    c,d,e = map(int,input().split())
    if b == 'min':
        print('Caso #'+str(i+1)+':',min(c,d,e))
    if b == 'max':
        print('Caso #'+str(i+1)+':',max(c,d,e))
    if b == 'mean':
        print('Caso #'+str(i+1)+':',(c+d+e)//3)
    if b == 'eye':
        print('Caso #'+str(i+1)+': '+'%d'%(0.30*c+0.59*d+0.11*e))    