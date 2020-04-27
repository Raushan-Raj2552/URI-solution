while True:
    a = int(input())
    if(a == 0):
        break
        
    b = ""
    for i in range(1,a+1):
        b += str(i)+" "
    print(b[:-1])
#[:-1] is used for removal of last whitespace