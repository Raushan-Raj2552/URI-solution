a = int(input())
c = []
for i in range(a):
    b = int(input())
    c.append(b)
if c[0] == max(c):
    print('S')
else:
    print('N')
        