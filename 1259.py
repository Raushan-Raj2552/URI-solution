a = int(input())
b = []
c = []
for i in range(a):
    d = int(input())
    if d%2 == 0:
        b.append(d)
    else:
        c.append(d)
b.sort()
c.sort(reverse = True)
for j in b:
    print(j)
for k in c:
    print(k)