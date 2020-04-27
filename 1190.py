c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[23])+float(c[34])+float(c[35])+float(c[45])+float(c[46])+float(c[47])+float(c[56])+float(c[57])+float(c[58])+float(c[59])+float(c[67])+float(c[68])+float(c[69])+float(c[70])+float(c[71])+float(c[79])+float(c[80])+float(c[81])+float(c[82])+float(c[83])+float(c[92])+float(c[93])+float(c[94])+float(c[95])+float(c[105])+float(c[106])+float(c[107])+float(c[118])+float(c[119])+float(c[131])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/30))