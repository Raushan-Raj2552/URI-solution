a,b,c = map(int,input().split())
d = max(a,b,c)
if (a+b+c-2*d)>0:
    if len({a,b,c})==1:
        print('Valido-Equilatero')
        if a*a+b*b+c*c-2*d*d==0:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    if len({a,b,c})==2:
        print('Valido-Isoceles')
        if a*a+b*b+c*c-2*d*d==0:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    if len({a,b,c})==3:
        print('Valido-Escaleno')
        if a*a+b*b+c*c-2*d*d==0:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
else:
    print('Invalido')