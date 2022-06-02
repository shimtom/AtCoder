N, M = [int(x) for x in input().split()]
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = input().split()
    edges[int(a)].append(int(b))


# O(N x (N + M))

answer = 0
for i in range(1, N + 1):
    # 各都市をスタートとして、繋がっている道路を辿る。
    stack = [i]
    memo = [False] * (N + 1)
    memo[i] = True

    while len(stack) > 0:
        end = stack.pop()
        for b in edges[end]:
            if not memo[b]:
                stack.append(b)
                memo[b] = True
    answer += sum(memo)

print(answer)
