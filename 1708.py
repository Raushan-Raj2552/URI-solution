import math as m
a,b = input().split()
c = int(b)-int(a)
x = m.ceil(int(b)/c)
#ceil represent smallest integer value greater thon or equal to.
print(x)