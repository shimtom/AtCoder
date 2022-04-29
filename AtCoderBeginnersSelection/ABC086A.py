a, b = [int(v) for v in input().split()]
ans = a * b
if ans % 2 == 1:
    print('Odd')
else:
    print('Even')
