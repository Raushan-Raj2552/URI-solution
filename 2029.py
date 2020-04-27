while True:
    try:
        vol = float(input())
        dia = float(input())
        rad = dia/2
        area = 3.14*(rad**2)
        hit = vol/(3.14*(rad**2))
        print('ALTURA = %.2f'%(hit))
        print('AREA = %.2f'%(area))
        
    except EOFError:
        break