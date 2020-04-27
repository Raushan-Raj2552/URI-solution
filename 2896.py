#Not understand problem but by checking cases that it is sum of quotient and remainder
a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = b%c
    e = b//c
    print(d+e)