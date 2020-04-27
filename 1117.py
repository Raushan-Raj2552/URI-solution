a = 0 #sum
b = 0 #number
while b < 2:
    c = float(input())
    if 0<=c<=10:
        a += c
        b += 1
    else:
        print("nota invalida")
print("media = %0.2f" %(a/2))