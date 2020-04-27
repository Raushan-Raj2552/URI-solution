a = int(input())
b = int(input())
c = []
d = []
for i in range(b):
    e = int(input())
    c.append(e)
for j in range(1,a+1):
    if j not in c:
        d.append(j)
print(len(d))