a,b,c,d=input().split(' ')
A=float(a)
B=float(b)
C=float(c)
D=float(d)
E=(A*2+B*3+C*4+D*1)/10
print('Media:',E)
if E>=7.0:
    print('Aluno aprovado.')
elif E<5.0:
    print('Aluno reprovado.')
elif 5.0<=E<=6.9:
    print('Aluno em exame.')
    F=float(input('Nota do exame: '))
    E=(E+F)/2
    if E>=5.0:
        print('Aluno aprovado')
    elif E<=4.9:
        print('Aluno reprovado')
    print('Media final:',(E))