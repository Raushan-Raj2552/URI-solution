a = int(input())
for i in range(a):
    b,c = map(str,input().split())
    d = b[::-1]
    e = c[::-1]
    if e in d:
        if e[0] == d[0]:
            print('encaixa')
        else:
            print('nao encaixa')
    else:
        print('nao encaixa')