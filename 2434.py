days,money = map(int,input().split())
ls = []
for i in range(days):
    addn = int(input())
    money+=addn
    ls.append(money)
print(min(ls))