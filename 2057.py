s,t,f = map(int,input().split())
if s==0:
    s==24
i = s+t+f
if i>24:
    print('%0.0f'%(i-24))
elif i==24:
    print('%0.0f'%(0))
else:
    print('%0.0f'%(i ))