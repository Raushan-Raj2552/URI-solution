a = 0
b = 0
for i in range(6):
    c = float(input())
    if c>0:
        a+=c
        b+=1
print(b,'valores positivos')
print('%0.1f'%(a/b))