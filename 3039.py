a = int(input())
b = 0
c = 0

for i in range(a):
    d,e = input().split()
    
    if e=='M':
        b+=1
    elif e=='F':
        c+=1
print(b,'carrinhos')
print(c,'bonecas')