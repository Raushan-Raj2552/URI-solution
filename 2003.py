while True:
    try:
        a,b = map(int,input().split(':'))
        late = 0
        if a>=7:
            hora = (a-7)*60
            late+=hora+b
        else:
            late+=0
        print('Atraso maximo:',late)
    except EOFError:
        break