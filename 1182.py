#%%
a = int(input())
b = str(input())
c = []
e = 0
for i in range(144):
    g = float(input())
    c.append(g)
if a!=11:
    for j in range(144):
        if j%12==(a+1):
            e+=c[j-1]
elif a==11:
    for k in range(144):
        if k%12==0:
            e+=c[k]
if b=='S':
    print('%0.1f'%(e))
elif b=='M':
    print('%0.1f'%(e/12))
#%%
c=int(input())
T=input()
sum=0
for i in range(144):
    a=float(input())
    if i%12==c:
        sum+=a;
if(T=="S"):
    print('%0.1f'%(sum))
else:
    print('%0.1f'%(sum/12))
