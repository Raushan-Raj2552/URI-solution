a = int(input())

for i in range(a):
    b,c,d,e = input().split()
    b = int(b)
    c = int(c)
    d = float(d)
    e = float(e)
    
    year = 0
    while(b<=c):
        B = int((b*d)/100)
        C = int((c*e)/100)
        year+= 1
        b += B
        c += C
        
        if(year > 100):
            break
    if(year > 100):
        print('Mais de 1 seculo.')
    else:
        print('%d'%(year),'anos.')