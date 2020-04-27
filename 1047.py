a,b,c,d=map(int, input().split())
if a==c and b==d:
    print('O JOGO DUROU',24,'HORA(S) E',0,'MINUTO(S)')
elif a==c and b<d:
    print('O JOGO DUROU',0,'HORA(S) E',d-b,'MINUTO(S)')
elif a==c and b>d:
    print('O JOGO DUROU',23,'HORA(S) E',d-b+60,'MINUTO(S)')
elif a<c and b==d:
    print('O JOGO DUROU',c-a,'HORA(S) E',0,'MINUTO(S)')
elif a<c and b<d:
    print('O JOGO DUROU',c-a,'HORA(S) E',d-b,'MINUTO(S)')
elif a<c and b>d:
    print('O JOGO DUROU',c-a-1,'HORA(S) E',60+d-b,'MINUTO(S)')
elif a>c and b==d:
    print('O JOGO DUROU',24+c-a,'HORA(S) E',0,'MINUTO(S)')
elif a>c and b<d:
    print('O JOGO DUROU',24+c-a,'HORA(S) E',d-b,'MINUTO(S)')
else:
    print('O JOGO DUROU',23+c-a,'HORA(S) E',60+d-b,'MINUTO(S)')

