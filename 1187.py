c = []
value = 0
command = str(input())
for i in range(144):
    a = float(input())
    c.append(a)
value+=float(c[1])+float(c[2])+float(c[3])+float(c[4])+float(c[5])+float(c[6])+float(c[7])+float(c[8])+float(c[9])+float(c[10])+float(c[14])+float(c[15])+float(c[16])+float(c[17])+float(c[18])+float(c[19])+float(c[20])+float(c[21])+float(c[27])+float(c[28])+float(c[29])+float(c[30])+float(c[31])+float(c[32])+float(c[40])+float(c[41])+float(c[42])+float(c[43])+float(c[53])+float(c[54])
if command == 'S':
    print('%0.1f'%(value))
elif command == 'M':
    print('%0.1f'%(value/30))