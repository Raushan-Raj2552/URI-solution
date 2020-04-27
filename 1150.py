import math as m
a = int(input())
while True:
    s = int(input())
    if s<=a:
        continue
    else:
        b = (((m.sqrt(((a-0.5)**2)+2*s))-a)+0.5)
        print(m.ceil(b))
        break