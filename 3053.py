a = int(input())
b = str(input())
for i in range(a):
    c = int(input())
    if (b=='B' and c==1) or (b=='A' and c==2) or (b=='C' and c==3):
        b='A'
    elif (b=='A' and c==1) or (b=='C' and c==2) or (b=='B' and c==3):
        b='B'
    elif (b=='C' and c==1) or (b=='B' and c==2) or (b=='A' and c==3):
        b='C'
print(b)