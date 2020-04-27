a,b = map(int,input().split())
for i in range(b):
    c = str(input())
    if c=='fechou':
        a+=1
    elif c=='clicou':
        a-=1
print(a)