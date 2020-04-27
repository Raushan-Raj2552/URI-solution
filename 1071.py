a=int(input())
b=int(input())
c=0
for n in range((b+1),a):
    if (n%2!=0):
        c+=n
print(c)