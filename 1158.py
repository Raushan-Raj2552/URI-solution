a = int(input())
for i in range(a):
    s = 0
    x,y=map(int,input().split())
    if x%2==0:
        s+=x*y+y*y
    else:
        s+=y*x+y*y-y
    print(s)