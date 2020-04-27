a = int(input())
for i in range(a):
    b = int(input())
    l = []
    for j in range(b):
        c = str(input())
        l.append(c)
    x = l.count(l[0])
    if x == b:
        print(l[0])
    else:
        print('ingles')