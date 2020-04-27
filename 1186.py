c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[23])+float(c[34])+float(c[35])+float(c[45])+float(c[46])+float(c[47])+float(c[56])+float(c[57])+float(c[58])+float(c[59])+float(c[67])+float(c[68])+float(c[69])+float(c[70])+float(c[71])+float(c[78])+float(c[79])+float(c[80])+float(c[81])+float(c[82])+float(c[83])+float(c[89])+float(c[90])+float(c[91])+float(c[92])+float(c[93])+float(c[94])+float(c[95])+float(c[100])+float(c[101])+float(c[102])+float(c[103])+float(c[104])+float(c[105])+float(c[106])+float(c[107])+float(c[111])+float(c[112])+float(c[113])+float(c[114])+float(c[115])+float(c[116])+float(c[117])+float(c[118])+float(c[119])+float(c[122])+float(c[123])+float(c[124])+float(c[125])+float(c[126])+float(c[127])+float(c[128])+float(c[129])+float(c[130])+float(c[131])+float(c[133])+float(c[134])+float(c[135])+float(c[136])+float(c[137])+float(c[138])+float(c[139])+float(c[140])+float(c[141])+float(c[142])+float(c[143])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/66))