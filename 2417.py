Cwin,Cdraw,Cdiff,Fwin,Fdraw,Fdiff = map(int,input().split())
if (Cwin*3+Cdraw) > (Fwin*3+Fdraw):
    print('C')
elif (Cwin*3+Cdraw) < (Fwin*3+Fdraw):
    print('F')
elif Cdiff > Fdiff:
    print('C')
elif Cdiff < Fdiff:
    print('F')
else:
    print('=')