a,b = list(map(int,input().split()))
c = 1
for i in range(1,((b//a)+1)):
    d = ""
    for j in range(a):
        d += str(c) + " "
        c += 1
    print(d[:-1])