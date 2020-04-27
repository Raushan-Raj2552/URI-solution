a = int(input())
b = str(input())
c = []
e = 0
f = 0
for i in range(144):
    g = float(input())
    c.append(g)
for j in range(12*a,(12*a)+12):
    e+=c[j]
    f+=1
if b=='S':
    print(e)
if b=='M':
    print(e/f)
