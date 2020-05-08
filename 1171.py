n = int(input())
lsx = []

for i in range(n):
    x = int(input())
    lsx.append(x)

setx = sorted(set(lsx))

count = []
for j in setx:
    count.append(lsx.count(j))

for i in range(len(count)):
    print(setx[i],"aparece",count[i],"vez(es)")