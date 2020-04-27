a = int(input())
b = 0
c = 0
d = 0
e = 0

for i in range(a):
    f,g = input().split()
    if g=="C":
        b += int(f)
        d += int(f)
    elif g=="R":
        b += int(f)
        c+= int(f)
    elif g=="S":
        b += int(f)
        e += int(f)

print('Total: %d'%(b),'cobaias')
print('Total de coelhos: %d'%(d))
print('Total de ratos: %d'%(c))
print('Total de sapos: %d' %(e))
print('Percentual de coelhos:','%0.2f'%((d/b)*100),'%')
print('Percentual de ratos:','%0.2f'%((c/b)*100),'%')
print('Percentual de sapos:','%0.2f'%((e/b)*100),'%')