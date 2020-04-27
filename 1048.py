a=float(input())
if 0<=a<=400.00:
    print('Novo salario: %1.2f'%(a*1.15))
    print('Reajuste ganho: %1.2f'%(a*0.15))
    print('Em percentual: 15 %')
elif 400.01<=a<=800.00:
    print('Novo salario: %1.2f'%(a*1.12))
    print('Reajuste ganho: %1.2f'%(a*0.12))
    print('Em percentual: 12 %')
elif 800.01<=a<=1200.00:
    print('Novo salario: %1.2f'%(a*1.10))
    print('Reajuste ganho: %1.2f'%(a*0.10))
    print('Em percentual: 10 %')
elif 1200.01<=a<=2000.00:
    print('Novo salario: %1.2f'%(a*1.07))
    print('Reajuste ganho: %1.2f'%(a*0.07))
    print('Em percentual: 7 %')
else:
    print('Novo salario: %1.2f'%(a*1.04))
    print('Reajuste ganho: %1.2f'%(a*0.04))
    print('Em percentual: 4 %')