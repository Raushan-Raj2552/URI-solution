a = int(input())
b = []
for i in range(a):
    c = str(input())
    d = c.upper()
    if d not in b:
        b.append(d)
e = 151-len(b)
print('Falta(m)',e,'pomekon(s).')