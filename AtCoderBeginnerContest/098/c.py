N = int(input())
S = input()

# 単純に全探索をするとO(N^2)で間に合わないので
# 累積和を利用してO(N)で高速に計算する

W = [0] * N
E = [0] * N
for i, s in enumerate(S):
    if s == 'W':
        W[i] = 1
    else:
        E[i] = 1

for i in range(1, N):
    W[i] += W[i - 1]
    E[i] += E[i - 1]

min_num = 10 ** 6
for i in range(N):
    left = 0
    if i - 1 > 0:
        left = W[i - 1]
    right = E[-1] - E[i]

    min_num = min(min_num, left + right)

print(min_num)
