import sys

N, M, X = [int(x) for x in input().split()]
C = []
A = []
for i in range(N):
    x = [int(x) for x in input().split()]
    C.append(x[0])
    A.append(x[1:])

# N <= 12 なので全探索が可能?
# 参考書の組み合わせは選ぶか選ばないかなのでO(2^N)
# 理解度が条件を満たすかを探索するのはO(NM)
# 全体は2^N x NM <= 589824
#
# DP問題としては？
# 現在の理解度の状態から逐次理解度を更新する方法は計算量が高すぎる
# また、A[m]同士で適切な比較演算が行えないので
# コスト最小にしつつ理解度を大きくするDP問題としては解けない

sum_A = [0 for _ in range(M)]
for a in A:
    sum_A = [x + y for x, y in zip(sum_A, a)]

if any([a < X for a in sum_A]):
    print(-1)
    sys.exit()


# Bit探索
min_cost = 10 ** 7
for i in range(2 ** N):
    cost = 0
    understandings = [0 for _ in range(M)]
    for index in range(N):
        if (i + 1) & 0b1 == 0b1:
            cost += C[index]
            understandings = [x + y for x, y in zip(understandings, A[index])]
        i >>= 1

    if all([a >= X for a in understandings]):
        min_cost = min(min_cost, cost)

print(min_cost)




# 深さ優先探索
# 単純に実装すると探索済みの部分も探索するので
# 計算量が非常に高い
# 探索済みの部分を単純に管理するとチェックに時間がかかる

# # cost, understandings, used references
# min_cost = 10 ** 7
# checkd = []
# stack = [(0, [0 for _ in range(M)], [])]
# while len(stack) > 0:
#     cost, understandings, refs = stack.pop()

#     if all([a >= X for a in understandings]):
#         min_cost = min(min_cost, cost)
#         continue

#     for i in range(N):
#         if i not in refs:
#             new_cost = cost + C[i]
#             new_understandings = [a + b for a, b in zip(understandings, A[i])]
#             new_refs = copy.copy(refs)
#             new_refs.append(i)

#             if new_refs not in checkd:
#                 stack.append((new_cost, new_understandings, new_refs))
#                 checkd.append(new_refs)

# print(min_cost)
