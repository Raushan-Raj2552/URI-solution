#formula = nC4 + nC2 + nC0
a = int(input())
b = ((a/24)*((a**3)-6*(a**2)+(23*a)-18)) + 1
print('%0.0f' %(b))
