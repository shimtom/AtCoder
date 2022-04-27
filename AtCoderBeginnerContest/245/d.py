N, M = [int(x) for x in input().split()]
A = [int(a) for a in input().split()]
C = [int(c) for c in input().split()]

a = A[0]
for n in range(N):
    if A[n] != 0:
        break

B = [0 for _ in range(M + 1)]
for i in range(M + 1 - n):
    b = C[n + i]

    for j in range(n + i):
        if i == j or i - j >= len(A):
            continue
        b -= A[i - j] * B[j]
    b /= A[n]
    B[i] = int(b)

print(' '.join([str(b) for b in B]))
