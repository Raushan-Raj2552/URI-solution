a,b,c,d,e,f,g,h,i = map(int,input().split())
if 1<=a<=10000:
    if 1<=b<=10000:
        if 1<=c<=10000:
            if 1<=d<=10000:
                if 1<=e<=10000:
                    if 1<=f<=10000:
                        if 1<=g<=10000:
                            if 1<=h<=10000:
                                if 1<=i<=10000:  
                                    if (a+b+c+d+e+f+g+h+i)%9==0:
                                        print('Rudolph') 
                                    if (a+b+c+d+e+f+g+h+i)%9==1:
                                        print('Dasher')
                                    if (a+b+c+d+e+f+g+h+i)%9==2:
                                        print('Dancer')
                                    if (a+b+c+d+e+f+g+h+i)%9==3:
                                        print('Prancer')
                                    if (a+b+c+d+e+f+g+h+i)%9==4:
                                        print('Vixen')
                                    if (a+b+c+d+e+f+g+h+i)%9==5:
                                        print('Comet')
                                    if (a+b+c+d+e+f+g+h+i)%9==6:
                                        print('Cupid')
                                    if (a+b+c+d+e+f+g+h+i)%9==7:
                                        print('Donner')
                                    if (a+b+c+d+e+f+g+h+i)%9==8:
                                        print('Blitzen')