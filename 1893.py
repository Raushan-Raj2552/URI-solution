a,b = map(int,input().split())

if( 0<=b<=2 ):
    print('nova')
elif( 97<=b<=100 ):
    print('cheia')
elif( b>a ):
    print('crescente')
else:
    print('minguante')