a = int(input())   
for i in range(a):  
    b = input()
    c,d = int(b[0]), int(b[2])
    e = b[1]
    if c==d:
        print(c*d)
    elif e.isupper():
        print(d-c)
    else:
        print(d+c)