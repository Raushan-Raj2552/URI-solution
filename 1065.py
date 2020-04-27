a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
even = []

for i in a,b,c,d,e:
    if i%2==0:
        even.append(i)
print(len(even),'valores pares')
