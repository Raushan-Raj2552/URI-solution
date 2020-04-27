p,n = map(int,input().split())
heit = input().split()
check = 0
for i in  range(len(heit)-1):
    if abs(int(heit[i])-int(heit[i+1]))<=p:
        check+=1
    else:
        check+=0
if check==n-1:
    print('YOU WIN')
else:
    print('GAME OVER')