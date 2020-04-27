import math
a,b,c = map(float, input().split())
D=((b**2)-(4*a*c))
if D>=0 and a!=0:
        E=(-b+math.sqrt(D))/(2*a)
        print('R1 = %1.5f'%(E))
        F=(-b-math.sqrt(D))/(2*a)
        print('R2 = %1.5f'%(F))
else:
        print('Impossivel calcular')

