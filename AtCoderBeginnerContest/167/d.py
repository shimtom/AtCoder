N, K = map(int, input().split())
A = list(map(int, input().split()))

# 単純にシミュレーションするとO(K)だがKが大きすぎる
# 何度もワープすると必ずどこかでループする
# よってループの開始までにK'回ワープし、その後、L回のワープでループするルートに入ったとすると、
# 結局、K' + K % L回のワープをシミュレーションすればよい
# 計算量はO(K)ただし、最悪O(N)

town = 0
visited = [False] * N
route = []
for _ in range(K):
    if visited[town]:
        index = route.index(town)
        loop = route[index:]
        town = loop[(K - index) % len(loop)]
        break

    visited[town] = True
    route.append(town)

    town = A[town] - 1

print(town + 1)
