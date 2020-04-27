import math as m
a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    print(m.ceil(b/c))