a = int(input())
d = 0
for i in range(a):
    b,c = map(int,input().split())
    if c<b:
        d+=c
print(d)