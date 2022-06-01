import math


def get_lcm(x, y):
    return (x * y) // math.gcd(x, y)


N, A, B = [int(x) for x in input().split()]


answer = N * (1 + N) // 2
if A < N:
    answer -= (N // A) * (A + N - N % A) // 2
if B < N:
    answer -= (N // B) * (B + N - N % B) // 2
if A < N and B < N:
    lcm = get_lcm(A, B)

    answer += (N // lcm) * (lcm + N - N % lcm) // 2
print(answer)
