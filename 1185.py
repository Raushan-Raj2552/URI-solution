c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[0])+float(c[1])+float(c[2])+float(c[3])+float(c[4])+float(c[5])+float(c[6])+float(c[7])+float(c[8])+float(c[9])+float(c[10])+float(c[12])+float(c[13])+float(c[14])+float(c[15])+float(c[16])+float(c[17])+float(c[18])+float(c[19])+float(c[20])+float(c[21])+float(c[24])+float(c[25])+float(c[26])+float(c[27])+float(c[28])+float(c[29])+float(c[30])+float(c[31])+float(c[32])+float(c[36])+float(c[37])+float(c[38])+float(c[39])+float(c[40])+float(c[41])+float(c[42])+float(c[43])+float(c[48])+float(c[49])+float(c[50])+float(c[51])+float(c[52])+float(c[53])+float(c[54])+float(c[60])+float(c[61])+float(c[62])+float(c[63])+float(c[64])+float(c[65])+float(c[72])+float(c[73])+float(c[74])+float(c[75])+float(c[76])+float(c[84])+float(c[85])+float(c[86])+float(c[87])+float(c[96])+float(c[97])+float(c[98])+float(c[108])+float(c[109])+float(c[120])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/66))