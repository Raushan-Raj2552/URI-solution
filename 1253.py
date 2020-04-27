a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = int(input())
for i in range(b):
    d = str(input())
    e = int(input())
    c = ''
    for j in d:
        f = a.find(j)
        c+=a[f-e]
    print(c)