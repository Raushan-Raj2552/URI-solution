a = int(input())
for i in range(a):
    b = int(input())
    if b>1:
        for i in range(2,b):
            if b%i == 0:
                print(b,'nao eh primo')
                break
        else:
            print(b,'eh primo')
    else:
        print(b,'nao eh primo')