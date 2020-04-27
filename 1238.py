a = int(input())
for i in range(a):
    c,d = input().split()
    b = ''
    e = len(c)
    f = len(d)
    if e<=f:
        for j in range(e):
            b+=c[j]+d[j]
        b+=d[e:]
#[e:] means for i>e
    elif f<e:
        for k in range(f):
            b+=c[k]+d[k]
        b+=c[f:]
    print(b)