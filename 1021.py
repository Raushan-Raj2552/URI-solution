N = float(input())
if 0 < N < 1000000.00:
    print('NOTAS:')
    a = N // 100
    print('%0.0f'%a,'nota(s) de R$ 100.00')
    b = N % 100
    c = b // 50
    print('%0.0f'%c,'nota(s) de R$ 50.00')
    d = b % 50
    e = d // 20
    print('%0.0f'%e,'nota(s) de R$ 20.00')
    f = d % 20
    g = f // 10
    print('%0.0f'%g,'nota(s) de R$ 10.00')
    h = f % 10
    i = h // 5
    print('%0.0f'%i,'nota(s) de R$ 5.00')
    j = h % 5
    k = j // 2
    print('%0.0f'%k,'nota(s) de R$ 2.00')
    print('MOEDAS:')
    l = j % 2
    m = l // 1
    print('%0.0f'%m,'moeda(s) de R$ 1.00')
    n = l % 1
    o = n // 0.5
    print('%0.0f'%o,'moeda(s) de R$ 0.50')
    p = n % 0.5
    q = p // 0.25
    print('%0.0f'%q,'moeda(s) de R$ 0.25')
    r = p % 0.25
    s = r // 0.10
    print('%0.0f'%s,'moeda(s) de R$ 0.10')
    t = r % 0.10
    u = t // 0.05
    print('%0.0f'%u,'moeda(s) de R$ 0.05')
    v = t % 0.05
    w = v // 0.01
    print('%0.0f'%w,'moeda(s) de R$ 0.01')