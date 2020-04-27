while True:
    a = int(input())
    if a==0:
        break
    elif a%2 == 0:
        print(5*(a+4))
    else:
        print(5*(a+5))