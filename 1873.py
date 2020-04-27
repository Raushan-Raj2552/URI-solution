a = int(input())
for i in range(a):
    b,c = input().split()
    if b=='tesoura' and c=='papel':
        print('rajesh')
    elif b=='papel' and c=='pedra':
        print('rajesh')
    elif b=='papel' and c=='lagarto':
        print('rajesh')
    elif b=='lagarto' and c=='spock':
        print('rajesh')
    elif b=='spock' and c=='tesoura':
        print('rajesh')
    elif b=='tesoura' and c=='lagarto':
        print('rajesh')
    elif b=='lagarto' and c=='papel':
        print('rajesh')
    elif b=='papel' and c=='spock':
        print('rajesh')
    elif b=='spock' and c=='pedra':
        print('rajesh')
    elif b=='pedra' and c=='tesoura':
        print('rajesh')
    elif c=='tesoura' and b=='papel':
        print('sheldon')
    elif c=='papel' and b=='pedra':
        print('sheldon')
    elif c=='papel' and b=='lagarto':
        print('sheldon')
    elif c=='lagarto' and b=='spock':
        print('sheldon')
    elif c=='spock' and b=='tesoura':
        print('sheldon')
    elif c=='tesoura' and b=='lagarto':
        print('sheldon')
    elif c=='lagarto' and b=='papel':
        print('sheldon')
    elif c=='papel' and b=='spock':
        print('sheldon')
    elif c=='spock' and b=='pedra':
        print('sheldon')
    elif c=='pedra' and b=='tesoura':
        print('sheldon')
    elif str(b)==str(c):
        print('empate')