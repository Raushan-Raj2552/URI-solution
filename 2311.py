n = int(input())
while n:
    n -= 1
    name = input()
    multiplier = float(input())
    point = [float(x) for x in input().split()]
    point = sum(sorted(point)[1:6]) * multiplier
    print('%s %.2f' % (name, point))
