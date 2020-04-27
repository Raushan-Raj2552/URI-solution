tim = int(input())
for i in range(tim):
    age = input().split()
    lenth = len(age)
    cptn = int((lenth/2))
    cptnage = age[cptn]
    print('Case',str(i+1)+':',cptnage)