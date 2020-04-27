from decimal import Decimal
a = 234.345
b = 45.698
print('%0.6f'%(a),'-','%0.6f'%(b))
print('%d'%(a),'-','%d'%(b))
print('%0.1f'%(a),'-','%0.1f'%(b))
print('%0.3f'%(a),'-','%0.3f'%(b))
print('%0.6e'%(Decimal(a)),'-','%0.6e'%(Decimal(b)))
print('%0.6E'%(Decimal(a)),'-','%0.6E'%(Decimal(b)))
print('%0.3f'%(a),'-','%0.3f'%(b))
print('%0.3f'%(a),'-','%0.3f'%(b))