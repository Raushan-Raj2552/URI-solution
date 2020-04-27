a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = 0
    if b<c:
        for j in range(b+1,c):
            if j%2==1:
                d+=(j)
        print(d)
    elif c<b:
        for j in range(c+1,b):
            if j%2==1:
                d+=(j)
        print(d)
    elif c==b:
        print('0')