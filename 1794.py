a = int(input())
b,c = map(int,input().split())
d,e = map(int,input().split())
if b<=a<=c:
    if d<=a<=e:
        print('possivel')
    else:
        print('impossivel')
else:
    print('impossivel')