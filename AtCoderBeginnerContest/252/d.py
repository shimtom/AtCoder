N = int(input())
A = [int(x) for x in input().split()]

# i < j < k かつ A[i] != A[j] != A[k]
# <-> A[i] < A[j] < A[k] となる(i, j, k)が一つだけ存在する

# jのとき、Aに含まれるA[j]未満の要素の数とA[j]以上の要素の数を掛けて、
# 組み合わせ数を求める

# 3 1 4 1
# a[j] = 1: 0 * 1 * 2
# a[j] = 3: 2 * 1 * 1
# a[j] = 4: 3 * 1 * 0

# Aに含まれる各要素の数を求める
counts = [0 for _ in range(2 * 10 ** 5 + 1)]
for a in A:
    counts[a] += 1

# A[j]以下の要素の合計数を求める
for a in range(2 * 10 ** 5):
    counts[a + 1] += counts[a]

answer = 0
for a in A:
    # jのときの A[i]以下の要素数 x A[k]以上の要素数
    # = A[j - 1]以下の要素数 x A[j + 1]以上の要素数
    # = A[j - 1]以下の要素数 x (N - A[j]以下の要素数)
    answer += counts[a - 1] * (N - counts[a])

print(answer)
