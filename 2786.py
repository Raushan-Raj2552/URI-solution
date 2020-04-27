L = int(input())
C = int(input())
if 1<=L<=100:
    if 1<=C<=100:
        print((L*C)+(L-1)*(C-1))
        print(2*(L+C-2))