while True:
    a,b = map(int,input().split())
    if(a <= 0 or b <= 0):
        break
    
    elif a>b:
        c = ""
        d = 0
        for i in range(b,a+1):
            c += str(i)+" "
            d+=i
        print(c[:-1],'Sum='+str(d))
    elif b>a:
        e = ""
        f = 0
        for i in range(a,b+1):
            e += str(i)+" "
            f+=i
        print(e[:-1],'Sum='+str(f))
#[:-1] is used for removal of last whitespace