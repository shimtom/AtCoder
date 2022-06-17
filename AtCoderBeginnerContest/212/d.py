import heapq

Q = int(input())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

# 単純にシミュレーションするとTLE
#
# 高速に要素の追加と最小値の取り出しを実現するために優先度付きキューを利用する。
# また、操作1でボールが追加される時に、操作2による将来的な値の変化量offsetを考慮する必要がある。
#
# 例えば、queries = [(1, X[0]), (2, X[1]), (1, X[2]), (2, X[3])]のとき、
# queries[0] -> [X[0]]
# queries[1] -> [X[0] + X[1]]
# queries[2] -> [X[0] + X[1], X[2]]
# queries[3] -> [X[0] + X[1] + X[3], X[2] + X[3]]
#
# 例えば、queries = [(1, X[0]), (2, X[1]), 3 (1, X[2]), (2, X[3])]のとき、
# queries[0] -> [X[0]]
# queries[1] -> [X[0] + X[1]]
# queries[2] -> []
# queries[3] -> [X[2]]
# queries[4] -> [X[2] + X[3]]
#
# つまり、X[i]に将来的に加えられる量はOffset[K] - Offset[i - 1]
# Offset[i]はiまでのoffsetの累積和。Kはpopされるタイミング
# つまり、pop時点をjとすると、popされる値は
#   X[i] + Offset[N] - Offset[i - 1] -(Offset[N] - Offset[j])
# = X[i] + Offset[j] - Offset[i - 1]

sums = [0] * Q
for i, q in enumerate(queries):
    if q[0] == 2:
        sums[i] = q[1]

for i in range(1, Q):
    sums[i] += sums[i - 1]

balls = []
heapq.heapify(balls)
for i, q in enumerate(queries):
    if q[0] == 1:
        x = q[1] - (sums[i - 1] if i - 1 > 0 else 0)
        heapq.heappush(balls, x)
    elif q[0] == 3:
        x = heapq.heappop(balls)
        print(x + sums[i])
