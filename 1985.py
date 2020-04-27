a = int(input())
b = 0
for i in range(a):
    x,y = map(float,input().split())
    if x==1001:
        b+=(1.50*y)
    if x==1002:
        b+=(2.50*y)
    if x==1003:
        b+=(3.50*y)
    if x==1004:
        b+=(4.50*y)
    if x==1005:
        b+=(5.50*y)
print('%0.2f'%b)
    