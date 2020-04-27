a = int(input())
for i in range(a):
    b = int(input())
    c = 0
    for i in range(1,b):
        if b%i==0:
            c+=i
    if c==b:
        print(b,'eh perfeito')
    else:
        print(b,'nao eh perfeito')