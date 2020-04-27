a,b,c,d=(input().split())
A=int(a)
B=int(b)
C=int(c)
D=int(d)
if D>A and B>C and C+D>A+B and C>0 and D>0 and A%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
