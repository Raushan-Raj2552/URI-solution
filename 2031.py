n = int(input())
while(n > 0):
    n -= 1
    p1 = str(input())
    p2 = str(input())
    if(p1 == 'ataque'):
        if(p2 == 'ataque'):
            print('Aniquilacao mutua')
        else:
            print('Jogador 1 venceu')
    elif(p1 == 'papel'):
        if((p2 == 'ataque') or (p2 == 'pedra')):
            print('Jogador 2 venceu')
        else:
            print('Ambos venceram')
    elif(p1 == 'pedra'):
        if(p2 == 'papel'):
            print('Jogador 1 venceu')
        if(p2 == 'ataque'):
            print('Jogador 2 venceu')
        elif(p2 == 'pedra'):
            print('Sem ganhador')
 