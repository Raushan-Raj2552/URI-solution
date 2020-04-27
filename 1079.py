a = int(input())
for i in range(a):
    x,y,z = list(map(float,input().split()))
    c = (x*2+y*3+z*5)/10
    print('%0.1f'%c)