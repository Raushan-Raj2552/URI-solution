X=int(input())
Y=int(input())
s=0
if(Y>X):
    for i in range(X,Y+1):
        if i%13!=0:
            s+=i
if(X>Y):
    for i in range(Y,X+1):
        if i%13!=0:
            s+=i
print(s)