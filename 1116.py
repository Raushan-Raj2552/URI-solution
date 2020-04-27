a = int(input())
for i in range(a):
    x,y = map(float,input().split())
    if x==0:
        print('0.0')
    elif y==0:
        print('divisao impossivel')
    else:
        print(x/y)