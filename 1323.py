while True:
    a = int(input())
    if a == 0 :
        break
    if a > 0 :
        b = 0
        for i in range(a+1):
            b += i**2
        print(b)