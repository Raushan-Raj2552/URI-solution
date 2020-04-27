a = int(input())
b = 0
c = 0
d = 0
e = 0
f = 0
for i in range(a):
    g,h = input().split()
    
    if h=='X':
        b+=1
    elif h=='H':
        c+=1
    elif h=='E':
        d+=1
    elif h=='A':
        e+=1
    elif h=='M':
        f+=1
print(b,'Hobbit(s)')
print(c,'Humano(s)')
print(d,'Elfo(s)')
print(e,'Anao(s)')
print(f,'Mago(s)')