a = input().split()
b = int(a[1])
c,d,e = map(int,input().split(':'))

f = input().split()
g = int(f[1])
h,i,j = map(int,input().split(':'))

day = g - b

hour = h - c
if(hour < 0):
    hour = 24 + hour
    day = day - 1

minute = i - d 
if(minute < 0):
    minute = 60 + minute
    hour = hour - 1

second = j - e
if(second < 0):
    second = 60 + second
    minute = minute - 1

if(day <= 0):
    day = 0

print("%d"%day,"dia(s)")
print("%d"%hour,"hora(s)")
print("%d"%minute, "minuto(s)")
print("%d"%second, "segundo(s)")
