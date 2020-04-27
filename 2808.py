alfabet = ' abcdefgh'
pos1,pos2 = input().split()
str1 = alfabet.find(pos1[0])
str2 = alfabet.find(pos2[0])
int1 = int(pos1[1])
int2 = int(pos2[1])
if (abs(str1-str2)==2 and abs(int1-int2)==1) or (abs(str1-str2)==1 and abs(int1-int2)==2):
    print('VALIDO')
else:
    print('INVALIDO')