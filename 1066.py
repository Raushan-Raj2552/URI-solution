a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
even = []
odd = []
positive = []
negative = []
for i in a,b,c,d,e:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

for i in a,b,c,d,e:
    if i>0:
        positive.append(i)
    if i<0:
        negative.append(i)
        
print(len(even),'valor(es) par(es)')
print(len(odd),'valor(es) impar(es)')
print(len(positive),'valor(es) positivo(s)')
print(len(negative),'valor(es) negativo(s)')