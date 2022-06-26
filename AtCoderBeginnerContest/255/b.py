N, K = [int(x) for x in input().split()]
A = [int(a) for a in input().split()]
X, Y = [], []
for _ in range(N):
    x, y = input().split()
    X.append(int(x))
    Y.append(int(y))

# 明かりを持っていない人への、明かりを持っている人達からの最短距離を求め、
# その中の最大値を求めればよい
# O(K * (N - K)) <= O(N^2)
B = [i + 1 for i in range(N) if i + 1 not in A]

distances = [None] * N

for a in A:
    sx, sy = X[a - 1], Y[a - 1]
    for b in B:
        x, y = X[b - 1], Y[b - 1]
        d = (x - sx) ** 2 + (y - sy) ** 2
        distances[b - 1] = (
            min(distances[b - 1], d) if distances[b - 1] is not None else d
        )

answer = max([d for d in distances if d is not None]) ** 0.5
print(answer)
