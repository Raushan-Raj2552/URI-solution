X,Y=input().split()
x=int(X)
y=int(Y)
if x==1:
    Result=4.00*y
elif x==2:
    Result=4.50*y
elif x==3:
    Result=5.00*y
elif x==4:
    Result=2.00*y
elif x==5:
    Result=1.50*y
print('Total: R$ %0.2f'%Result)