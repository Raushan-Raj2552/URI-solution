a=float(input())
if 0.00<=a<=2000.00:
    print('Isento')
elif 2000.01<=a<=3000.00:
    b=(a-2000)
    print('R$ %0.2f'%(b*0.08))
elif 3000.01<=a<=4500.00:
    b=(a-3000)
    print('R$ %0.2f'%(b*0.18+1000*0.08))
else :
    b=(a-4500)
    print('R$ %0.2f'%(b*0.28+0.18*1500+1000*0.08))