a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    if d==1:
        print('%02.0f'%(b)+':'+'%02.0f'%(c)+' - A porta abriu!')
    elif d==0:
        print('%02.0f'%(b)+':'+'%02.0f'%(c)+' - A porta fechou!')