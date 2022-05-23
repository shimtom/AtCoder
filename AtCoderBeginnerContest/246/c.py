from math import ceil

def discount(prices, coupon, num, waste=False):
    """ 無駄にならない範囲でクーポンを適用"""
    discounteds = []
    for p in sorted(prices, reverse=True):
        if waste:
            n = min(int(ceil(p / coupon)), num)
        else:
            n = min(p // coupon, num)
        discounteds.append(max(p - n * coupon, 0))
        num -= n

    return discounteds, num

N, K, X = input().split()
As = input().split()

N = int(N)
K = int(K)
X = int(X)
As = [int(A) for A in As]

As, K = discount(As, X, K, waste=False)
As, K = discount(As, X, K, waste=True)

print(sum(As))
