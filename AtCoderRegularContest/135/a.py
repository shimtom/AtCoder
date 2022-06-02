import math

X = int(input())

# 1 <= x <= 10^18の範囲でfloor(x / 2) * ceil(x / 2) が元のxより小さくなる場合は
# x = 1, 2, 3のときのみ。
# よって、操作を行なった結果が3より大きい場合には操作を繰り返す。
# また、操作の結果、同じ値が黒板に書かれる場合が頻出するのでメモも利用して効率的に計算する。

memo = dict()
def op(x):
    if x <= 3:
        return x
    if x in memo:
        return memo[x]
    floor = x // 2
    ceil = x // 2 + x % 2
    result = (op(floor) * op(ceil)) % 998244353
    if x not in memo:
        memo[x] = result
    return result

answer = op(X) % 998244353

print(answer)
