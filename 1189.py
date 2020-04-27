c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[12])+float(c[24])+float(c[25])+float(c[36])+float(c[37])+float(c[38])+float(c[48])+float(c[49])+float(c[50])+float(c[51])+float(c[60])+float(c[61])+float(c[62])+float(c[63])+float(c[64])+float(c[72])+float(c[73])+float(c[74])+float(c[75])+float(c[76])+float(c[84])+float(c[85])+float(c[86])+float(c[87])+float(c[96])+float(c[97])+float(c[98])+float(c[108])+float(c[109])+float(c[120])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/30))