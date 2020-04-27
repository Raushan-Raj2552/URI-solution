a = int(input())

for i in range(a):
    b = str(input())
    c = ''
    if len(b)==20:
        if b[0]=='R' and b[1]=='A':
            for j in range(2,len(b)):
                c+=b[j]
            print(int(c))
        else:
            print('INVALID DATA')
    else:
        print('INVALID DATA')