c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[12])+float(c[24])+float(c[25])+float(c[36])+float(c[37])+float(c[38])+float(c[48])+float(c[49])+float(c[50])+float(c[51])+float(c[60])+float(c[61])+float(c[62])+float(c[63])+float(c[64])+float(c[72])+float(c[73])+float(c[74])+float(c[75])+float(c[76])+float(c[77])+float(c[84])+float(c[85])+float(c[86])+float(c[87])+float(c[88])+float(c[89])+float(c[90])+float(c[96])+float(c[97])+float(c[98])+float(c[99])+float(c[100])+float(c[101])+float(c[102])+float(c[103])+float(c[108])+float(c[109])+float(c[110])+float(c[111])+float(c[112])+float(c[113])+float(c[114])+float(c[115])+float(c[116])+float(c[120])+float(c[121])+float(c[122])+float(c[123])+float(c[124])+float(c[125])+float(c[126])+float(c[127])+float(c[128])+float(c[129])+float(c[132])+float(c[133])+float(c[134])+float(c[135])+float(c[136])+float(c[137])+float(c[138])+float(c[139])+float(c[140])+float(c[141])+float(c[142])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/66))