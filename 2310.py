a = int(input())
ss = 0
ss1 = 0
sb = 0
sb1 = 0
sa = 0
sa1 = 0
for i in range(a):
    name = str(input())
    s,b,a = map(int,input().split())
    s1,b1,a1 = map(int,input().split())
    ss+=s
    ss1+=s1
    sb+=b
    sb1+=b1
    sa+=a
    sa1+=a1
print('Pontos de Saque:','%0.2f'%((ss1/ss)*100),'%.')
print('Pontos de Bloqueio:','%0.2f'%((sb1/sb)*100),'%.')
print('Pontos de Ataque:','%0.2f'%((sa1/sa)*100),'%.')