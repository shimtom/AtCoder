import sys

N = int(input())
C = []
for _ in range(N):
    line = input()
    C.append([int(c) for c in line.split()])


# Aの要素のどれかが決まるとBの要素の全てが定まり、Bの要素が定まるとAの残りの要素も決まる。
# A,Bが条件を満たしており、そのときのAの最小値がM(M > 0)のとき、
# Bの全要素にMを加算し、Aの最小値からMを減算しても条件を満たすので、Aの最小値は0で固定してよい。
# A[i'] = 0のとき、A[i] = C[i][j] - C[i'][j] (i != i')なのでC[i][j] >= C[i'][j]が常に成り立つ必要がある。
# そのため、i'はC[i'][j]が最小となるインデックスになる。
# よって、Cが最小となるインデックスi'を求めて対応するA[i']=0とし、このときのBを求める。
# 次にBからAを求め、求めたA,Bが本来の条件を満たすかを確認すればよい。
#
# O(2xN^2 + 2N) = O(N^2): N <= 500なので十分に解ける

A = [-1] * N
B = [-1] * N

# get min indices
min_value = 10 ** 9 + 1
min_i, min_j = -1, -1
for i in range(N):
    for j in range(N):
        if C[i][j] < min_value:
            min_value = C[i][j]
            min_i = i
            min_j = j


# calc B
A[min_i] = 0
for j in range(N):
    # B[j] = C[min_i][j] - A[min_i], A[min_i]は0なので省略
    B[j] = C[min_i][j]

# calc A
for i in range(N):
    A[i] = C[i][0] - B[0]

# check
for i in range(N):
    for j in range(N):
        if C[i][j] != A[i] + B[j] or A[i] < 0 or B[j] < 0:
            print('No')
            sys.exit()

print('Yes')
print(*A)
print(*B)
