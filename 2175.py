a,b,c = map(float,input().split())
if b<c and b<a :
    print('Bruno')
elif c<a and c<b :
    print('Ian')
elif a<c and a<b :
    print('Otavio')
else:
    print('Empate')