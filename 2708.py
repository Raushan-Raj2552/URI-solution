a = 0
b = 0
while True:
    c = input().split()
    if c[0] == 'ABEND':
        break
    if c[0] == 'SALIDA':
        b += 1
        a+=int(c[1])
    else:
        b -= 1
        a-=int(c[1])
print(a)
print(b)