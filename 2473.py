a = input().split()
b = input().split()
c = 0
for i in a:
    if i in b:
        c+=1
if c==0 or c==1 or c==2:
    print('azar')
elif c==3:
    print('terno')
elif c==4:
    print('quadra')
elif c==5:
    print('quina')
elif c==6:
    print('sena')