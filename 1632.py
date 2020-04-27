t = int(input())
for i in range(t):
    s1 = str(input())
    l = len(s1)
    a = 0
    b = 0
    a+=s1.count('a')
    a+=s1.count('e')
    a+=s1.count('i')
    a+=s1.count('o')
    a+=s1.count('s')
    a+=s1.count('A')
    a+=s1.count('E')
    a+=s1.count('I')
    a+=s1.count('O')
    a+=s1.count('S')
    if a>0:
        b+=((2**(l-a))*(3**(a)))
    else:
        b+=(2**l)
    print(b)