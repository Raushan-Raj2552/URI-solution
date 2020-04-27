while True:
    a = int(input())
    if a == 0 :
        break
    if a > 0 :
        for i in range(a):
            b = int(input())
            if b%2 == 0:
                print(2*b-2)
            else:
                print(2*b-1)