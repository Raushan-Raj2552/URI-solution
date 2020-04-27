a = int(input())
b = int(input())
d = 0
for i in range(b):
    c = int(input())
    if c*a >= 40000000:
        d+=1
print(d)