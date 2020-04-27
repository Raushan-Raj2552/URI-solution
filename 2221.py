t = int(input())
for i in range(t):
    b = int(input())
    v1 = 0
    v2 = 0
    
    a1,d1,l1 = map(int,input().split())
    a2,d2,l2 = map(int,input().split())
    if l1%2==0 and l2%2==1:
        v1 += (a1+d1+2*b)/2
        v2 += (a2+d2)/2
    elif l1%2==0 and l2%2==0:
        v1 += (a1+d1+2*b)/2
        v2 += (a2+d2+2*b)/2
    elif l1%2==1 and l2%2==0:
        v1 += (a1+d1)/2
        v2 += (a2+d2+2*b)/2
    elif l1%2==1 and l2%2==1:
        v1 += (a1+d1)/2
        v2 += (a2+d2)/2
    
    if v1>v2:
        print('Dabriel')
    elif v1<v2:
        print('Guarte')
    elif v1==v2:
        print('Empate')