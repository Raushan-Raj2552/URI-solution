for i in range(0,21):
    if i==0:
        print('I=0','J=1')
        print('I=0','J=2')
        print('I=0','J=3')
    elif i==10:
        print('I=1','J=2')
        print('I=1','J=3')
        print('I=1','J=4')
    elif i==20:
        print('I=2','J=3')
        print('I=2','J=4')
        print('I=2','J=5')
    elif i%2==0:
        print('I='+str(i/10),'J='+str((i/10)+1))
        print('I='+str(i/10),'J='+str((i/10)+2))
        print('I='+str(i/10),'J='+str((i/10)+3))