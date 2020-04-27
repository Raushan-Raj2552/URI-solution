a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    print(len(str(b**c)))