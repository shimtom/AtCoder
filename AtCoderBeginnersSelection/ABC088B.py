N = int(input())
a = [int(v) for v in input().split()]
a = sorted(a, reverse=True)

A, B = [], []
for i, n in enumerate(a):
    if i % 2 == 0:
        A.append(n)
    else:
        B.append(n)

print(sum(A) - sum(B))
