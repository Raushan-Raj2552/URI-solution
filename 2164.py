import math as m
n = int(input())
if 0<n<=50:
    b = (1+m.sqrt(5))/2
    c = (1-m.sqrt(5))/2
    d = m.sqrt(5)
    f = ((b**n)-(c**n))/d
print('%0.1f'%f)
    