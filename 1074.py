a = int(input())

for i in range(a):
    d = int(input())
    if d==0:
        print('NULL')
    elif d>0:
        if d%2==0:
            print('EVEN POSITIVE')
        if d%2!=0:
            print('ODD POSITIVE')
    elif d<0:
        if d%2==0:
            print('EVEN NEGATIVE')
        if d%2!=0:
            print('ODD NEGATIVE')