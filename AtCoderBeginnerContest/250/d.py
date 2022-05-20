import math

N = int(input())

def get_primes(n):
    if n < 2:
        return []

    primes = []

    # Sieve of Eratosthenes
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(n + 1):
        if not is_prime[i]:
            continue

        primes.append(i)

        for j in range(i, n + 1, i):
            is_prime[j] = False

    return primes


primes = get_primes(10 ** 6)

answer = 0

last_index = len(primes)
for i, p in enumerate(primes):
    for j in reversed(range(last_index)):
        q = primes[j]
        if p < q and p * q ** 3 <= N:
            answer += j - i
            last_index = j + 1
            break
    else:
        break

print(answer)
