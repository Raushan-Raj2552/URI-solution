a = int(input())
for i in range(a):
    b = str(input())
    if len(b)==3:
        if (b[0]=='o' and b[1]=='n') or (b[0]=='o' and b[2]=='e') or  (b[1]=='n' and b[2]=='e'):
            print('1')
        elif (b[0]=='t' and b[1]=='w') or (b[0]=='t' and b[2]=='o') or  (b[1]=='w' and b[2]=='o'):
            print('2')
    else:
        print('3')