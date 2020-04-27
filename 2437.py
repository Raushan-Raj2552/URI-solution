a,b,c,d = map(int,input().split())
e = 0
if a <= c:
    e += (c-a)
else:
    e += (a-c)
if b <= d:
    e += (d-b)
else:
    e += (b-d)
print(e)