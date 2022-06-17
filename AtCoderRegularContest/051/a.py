x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

# Yes, NoではなくYES, NOを出力しなければならないことに注意！


def f(x, y):
    return x ** 2 + y ** 2


# 赤く塗られた部分が存在するか
if x1 - r < x2 or x1 + r > x3 or y1 - r < y2 or y1 + r > y3:
    print('YES')
else:
    print('NO')

# 青く塗られた部分が存在するか
r2 = r ** 2
m1 = f(x2 - x1, y2 - y1)
m2 = f(x3 - x1, y2 - y1)
m3 = f(x2 - x1, y3 - y1)
m4 = f(x3 - x1, y3 - y1)
if m1 > r2 or m2 > r2 or m3 > r2 or m4 > r2:
    print('YES')
else:
    print('NO')
