while True:
    a = int(input())
    if a == 0:
        break
    else:
        b = input().split()
        m = 0
        j = 0
        for i in b:
            if i=='0':
                m+=1
            elif i=='1':
                j+=1
        print('Mary won',m,'times and John won',j,'times')