a = int(input())
for i in range(a):
    h,d,g = map(int,input().split())
    if 200<=h<=300 :
        if 50<=d :
            if 150<=g :
                print('Sim')
            else:
                print('Nao')
        else:
            print('Nao')
    else:
        print('Nao')