a,b,c = map(int,input().split())
d,e,f = map(int,input().split())
if d>a:
    C = d-a
else:
    C = 0

if e>b:
    B = e-b
else:
    B = 0
if f>c:
    P = f-c
else:
    P = 0
print(C+B+P)