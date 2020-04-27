L = int(input())
C = int(input())
if 1<=L<=1000:
    if 1<=C<=1000:
        if L%2==0:
            if C%2==0:
                print('1')
            else:
                print('0')
        if L%2!=0:
            if C%2!=0:
                print('1')
            else:
                print('0')
        
        