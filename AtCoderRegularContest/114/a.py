import math

N = int(input())
X = list(map(int, input().split()))

# X[i]とaが互いに素ではない <-> X[i]とaの公約数が1以外に存在する。
# aが最小である為には、aとX[i]との1以外の公約数が素数であればよい。


def get_primes(n):
    # Sieve of Eratosthenes
    table = [True] * (n + 1)
    table[0] = False
    table[1] = False

    for i in range(2, n + 1):
        if table[i]:
            for j in range(i + 1, n + 1):
                if j % i == 0:
                    table[j] = False

    primes = [i for i in range(n + 1) if table[i]]

    return primes


primes = get_primes(max(X))

answer = None
for i in range(2 ** len(primes)):
    factors = [primes[j] for j in range(len(primes)) if (i & 1 << j) > 0]
    is_coprime = [False] * N
    for p in factors:
        for j, x in enumerate(X):
            is_coprime[j] = is_coprime[j] or x % p == 0

    if all(is_coprime):
        if answer is None:
            answer = math.prod(factors)
        else:
            answer = min(answer, math.prod(factors))

print(answer)
