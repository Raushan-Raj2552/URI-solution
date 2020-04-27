c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[89])+float(c[90])+float(c[100])+float(c[101])+float(c[102])+float(c[103])+float(c[111])+float(c[112])+float(c[113])+float(c[114])+float(c[115])+float(c[116])+float(c[122])+float(c[123])+float(c[124])+float(c[125])+float(c[126])+float(c[127])+float(c[128])+float(c[129])+float(c[133])+float(c[134])+float(c[135])+float(c[136])+float(c[137])+float(c[138])+float(c[139])+float(c[140])+float(c[141])+float(c[142])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/30))