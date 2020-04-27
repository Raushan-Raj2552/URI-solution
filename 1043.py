a,b,c=(input().split())
A=float(a)
B=float(b)
C=float(c)
if A+B>C and B+C>A and A+C>B:
    print('Perimetro = %1.1f'%(A+B+C))
else:
    D=(C*(A+B))/2
    print('Area = %1.1f'%(D))