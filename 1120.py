while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    b1 = str(b)
    
    b2 = b1.replace(str(a),'')
    if b2=='' or int(b2)==0 :
        out = 0
    else:
        out = int(b2)
    print(out)