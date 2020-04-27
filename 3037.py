a = int(input())
for i in range(a):
    john = 0
    mary = 0
    b,c = map(int,input().split())
    john+=(b*c)
    d,e = map(int,input().split())
    john+=(d*e)
    f,g = map(int,input().split())
    john+=(f*g)
    h,i = map(int,input().split())
    mary+=(h*i)
    j,k = map(int,input().split())
    mary+=(j*k)
    l,m = map(int,input().split())
    mary+=(l*m)
    if john>mary:
        print('JOAO')
    else:
        print('MARIA')