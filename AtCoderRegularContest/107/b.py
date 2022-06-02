N, K = [int(x) for x in input().split()]

# 1 <= a, b, c, d <= N かつ a + b - c - d = K
# A = a + b, C =  c + d (2 <= A, B <= 2N)と置くと A - C = Kなので
# O(N)でA, Cを列挙できる。
# x = a + b or c + dとすると1 <= a, b, c, d <= N での(a, b), (c, d)の組み合わせは
# min(x -1, 2N - x + 1)通り
#
# よって、A, Cを列挙しつつ、組み合わせを数えればO(N)で求められる。

# N == 4, x = 9
# 1, 2, 3, 4,|| 5, 6, 7, 8
# N == 5, x = 9
# 1, 2, 3, |4,|| 5,| 6, 7, 8
# N == 6, x = 9
# 1, 2, |3, 4, 5, 6,| 7, 8



answer = 0
for x in range(2, 2 * N + 1):
    answer += max(min(x - 1, 2 * N - x + 1) * min(x - K - 1, 2 * N - (x - K) + 1), 0)

print(answer)
