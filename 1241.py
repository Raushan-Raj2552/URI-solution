a = int(input())
for i in range(a):
    b,c = input().split()
    if c in b:
        print('encaixa')
    else:
        print('nao encaixa')