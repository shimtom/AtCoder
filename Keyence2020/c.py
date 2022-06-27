N, K, S = [int(x) for x in input().split()]

# K <= Nでl = r が許されるので、各要素の値がSである長さKの配列を作成し、
# N - Kの長さで、どの範囲の合計もSとならない配列を繋げればよい。
# 繋げる配列は 1 <= A[n] <= 10 ** 9 を満たす必要があるので、
# 例えば、S < 10^9 のときはA[n] = S + 1とすればよい。
# S = 10^9 のときはA[n] = 1 とすればよい。（K <= N <= 10^5 なので、1 x (N -K) は必ずS未満）　
A = [S] * K
if S < 10 ** 9:
    A += [S + 1] * (N - K)
else:
    A += [1] * (N - K)

print(*A)
