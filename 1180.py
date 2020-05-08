a = int(input())
b = map(int,input().split())
lsb = list(b)
minimum = min(lsb)
index = lsb.index(minimum)

print("Menor valor:",minimum)
print("Posicao:",index)