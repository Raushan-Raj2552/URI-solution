a = 0
b = 0
while True:
    c = int(input())
    if c<0:
        break
    if c>=0:
        a+=c
        b+=1
print('%0.2f'%(a/b))