b = 0
a = int(input())
for i in range(a):
    t,v = map(int,input().split())
    b += (t*v)
print(b)