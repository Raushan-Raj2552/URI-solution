a = int(input())
for i in range(a):
    b = int(input())
    R = 0
    G = 0
    B = 0
    for i in range(b):
        c,d = input().split()
        if c=='G' and d=='R':
            G+=1
        elif c=='G' and d=='B':
            G+=2
        elif c=='B' and d=='R':
            B+=2
        elif c=='B' and d=='G':
            B+=1
        elif c=='R' and d=='G':
            R+=2
        elif c=='R' and d=='B':
            R+=1
    if R>G and R>B:
        print('red')
    elif G>B and G>R:
        print('green')
    elif B>R and B>G:
        print('blue')
    elif R==G==B:
        print('trempate')  
    elif G==R or R==B or B==G:
        print('empate')