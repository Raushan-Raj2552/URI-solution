while True:
    try:
        x,y=map(int,input().split())
        if x==0 or y==0:
            break
        if x>0 and y>0:
            print('primeiro')
        if x<0 and y>0:
            print('segundo')
        if x<0 and y<0:
            print('terceiro')
        if x>0 and y<0:
            print('quarto')
    except:
        break