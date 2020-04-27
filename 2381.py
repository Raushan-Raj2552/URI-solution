n,k = map(int,input().split())
a = []
for i in range(n):
    name = str(input())
    a.append(name)
b = a.sort()
print(a[k-1])