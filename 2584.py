import math as m
a = int(input())
for i in range(a):
    b = int(input())
    c = (0.25*m.sqrt(5*(5+2*m.sqrt(5))))*b*b
    print('%0.3f'%c)