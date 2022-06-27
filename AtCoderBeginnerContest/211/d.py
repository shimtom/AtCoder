N, M = [int(x) for x in input().split()]
A, B = [], []
for _ in range(M):
    a, b = input().split()
    A.append(int(a))
    B.append(int(b))

edges = [[] for _ in range(N)]
for a, b in zip(A, B):
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

# 幅優先探索を利用すれば、
# Edgeのコストが全て1なのである頂点が初めて出現したときが、その頂点までの最短経路となる。
# O(M)
costs = [None] * N
costs[0] = 0
counts = [0] * N
counts[0] = 1

queue = [0]
while len(queue) > 0:
    n = queue.pop(0)
    for i in edges[n]:
        if costs[i] is None:
            costs[i] = costs[n] + 1
            counts[i] = counts[n]
            queue.append(i)
        elif costs[i] == costs[n] + 1:
            counts[i] = (counts[i] + counts[n]) % (10 ** 9 + 7)

print(counts[-1])
