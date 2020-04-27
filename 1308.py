import math as m
a = int(input())
for i in range(a):
    b = int(input())
    c = m.sqrt(1+(8*b))
    d = (c-1)/2
    print('%0.0f'%(d//1))