N = int(input())
if 0 < N < 1000000:
    print(N)
    a = N // 100
    print('{} nota(s) de R$ 100,00'.format(a))
    b = N % 100
    c = b // 50
    print('{} nota(s) de R$ 50,00'.format(c))
    d = b % 50
    e = d // 20
    print('{} nota(s) de R$ 20,00'.format(e))
    f = d % 20
    g = f // 10
    print('{} nota(s) de R$ 10,00'.format(g))
    h = f % 10
    i = h // 5
    print('{} nota(s) de R$ 5,00'.format(i))
    j = h % 5
    k = j // 2
    print('{} nota(s) de R$ 2,00'.format(k))
    l = j % 2
    m = l // 1
    print('{} nota(s) de R$ 1,00'.format(m))
