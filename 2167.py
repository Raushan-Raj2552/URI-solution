a = int(input())
b = list(input().split())
c = []
for i in range(1,len(b)): 
    if int(b[i])<int(b[i-1]):
        c.append(i+1)
if len(c)>0:
    print(min(c))
else:
    print('0')