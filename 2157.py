a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = ''
    for i in range(b,c+1):
        d += str(i)
    print(d+d[::-1])