a=int(input())
if 5<a<2000:
    for i in range(1,a+1):
        if i%2==0:
            print(i,'^2 = ',i**2,sep='')
