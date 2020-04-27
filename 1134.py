b = 0
c = 0
d = 0
while True:
    a = int(input())
    if a==4:
        break
    elif a>4 or a<1:
        continue
    elif a == 1:
        b+=1
    elif a == 2:
        c+=1
    elif a == 3:
        d+=1
print('MUITO OBRIGADO')
print('Alcool:',b)
print('Gasolina:',c)
print('Diesel:',d)