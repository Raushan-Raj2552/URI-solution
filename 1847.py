a,b,c = map(int,input().split())
if (a>b):
    if (c>b):
        print(':)')
    else:
        if (b-c<a-b):
            print(':)')
        else:
            print(':(')
            
    
elif (a<b):
    if (c<b):
        print(':(')
    else:
        if (b-c>a-b):
            print(':(')
        else:
            print(':)')
    
else:
    if (c>a):
        print(':)')
    else:
        print(':(')