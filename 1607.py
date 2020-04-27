al = 'abcdefghijklmnopqrstuvwxyz'
a = int(input())
for i in range(a):
    b,c = input().split()
    x = 0
    for i in range(len(b)):
        d = (al.find(c[i])-al.find(b[i]))
        if d>=0:
            x+=d
        else:
            x+=(d+26)
    print(x)