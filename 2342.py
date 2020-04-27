n = int(input())
p,c,q = input().split()
if c == '+' and int(p)+int(q) <= n:
    print('OK')
elif c == '*' and int(p)*int(q) <= n:
    print('OK')
else:
    print('OVERFLOW')