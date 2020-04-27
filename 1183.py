c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[1])+float(c[2])+float(c[3])+float(c[4])+float(c[5])+float(c[6])+float(c[7])+float(c[8])+float(c[9])+float(c[10])+float(c[11])+float(c[14])+float(c[15])+float(c[16])+float(c[17])+float(c[18])+float(c[19])+float(c[20])+float(c[21])+float(c[22])+float(c[23])+float(c[27])+float(c[28])+float(c[29])+float(c[30])+float(c[31])+float(c[32])+float(c[33])+float(c[34])+float(c[35])+float(c[40])+float(c[41])+float(c[42])+float(c[43])+float(c[44])+float(c[45])+float(c[46])+float(c[47])+float(c[53])+float(c[54])+float(c[55])+float(c[56])+float(c[57])+float(c[58])+float(c[59])+float(c[66])+float(c[67])+float(c[68])+float(c[69])+float(c[70])+float(c[71])+float(c[79])+float(c[80])+float(c[81])+float(c[82])+float(c[83])+float(c[92])+float(c[93])+float(c[94])+float(c[95])+float(c[105])+float(c[106])+float(c[107])+float(c[118])+float(c[119])+float(c[131])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/66))