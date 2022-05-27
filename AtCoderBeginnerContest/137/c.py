import math

N = int(input())
S = []
for _ in range(N):
    S.append(input())

# 文字列s1とs2がアナグラムであるかはsortした文字列同士が一致するかで判定可能
# 文字列数は10なので高速に判定可能

# 全探索するとO(N^2)でN<=10^5なので終わらない
# 文字列をsortすれば同一の文字列の数がO(N)でわかる
# そこから組み合わせの数を求めればよい
# O(N * 10log10 + NlogN + N) = O(N + NlogN)

for i, s in enumerate(S):
    S[i] = sorted(s)
S = sorted(S)

answer = 0
index = 0
while index < len(S):
    s = S[index]
    count = 0
    while index + count < len(S) and s == S[index + count]:
        count += 1

    if count > 1:
        answer += math.comb(count, 2)

    index += count

print(answer)
