import math
from functools import reduce

N = int(input())
A = [int(a) for a in input().split()]

# Aの最小公倍数 - 1の数に対してfは最大となる


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def comp_lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def f(m):
    return sum([m % a for a in A])


lcm = comp_lcm(*A)
print(f(lcm - 1))
