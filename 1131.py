Inter = 0
Gremio = 0
Empates = 0
a = 0
while True:
    g1,g2 = map(int,input().split())
    print('Novo grenal (1-sim 2-nao)')
    a+=1
    repeat = int(input())
    if g1 == g2:
        Empates+=1
    elif g1<g2:
        Gremio+=1
    elif g1>g2:
        Inter+=1
    if repeat == 1:
        continue
    elif repeat==2:
        break
print(a,'grenais')
print('Inter:'+str(Inter))
print('Gremio:'+str(Gremio))
print('Empates:'+str(Empates))
print('Inter venceu mais')