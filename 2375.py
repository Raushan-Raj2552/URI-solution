dia = int(input())
lenth,breath,heit = map(int,input().split())
if min(lenth,breath,heit) < dia:
    print('N')
else:
    print('S')