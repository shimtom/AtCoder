import sys

N, K = [int(x) for x in input().split()]
A = [int(a) for a in input().split()]

# A = a[0], ..., a[i], ..., a[N - 1]に対し、
# 任意のiとi + K番目の交換を何度でも行うことでソートが可能ということは、
# Aの部分集合A' = a[i], a[i + K], a[i + 2 * K], ... のみをソートしたあとに結合した配列が
# ソートしたAと一致するということ。
# 方法1:
#   A'をi=0...K-1の範囲で求め、それぞれの配列をソートし、再結合後、元の配列をソートした結果と比較する。
#   O(N log N) + O(ceil(N / K) * K log K) + O(K) + O(N) = O(N log N) + O(N log K) + O(N)
# 方法2:
#   Aをソートした配列を用意し、元の配列の要素A[i]がA[i + j * K]のどれかに一致するかを調べる。
#   ただし、A'に同じ値が含まれることを考慮し、判定時に同じ値が必要数あることを調べる必要がある。
# 方法3: 採用
#   元の配列とAをソートした配列を用意し、それぞれでa[i + j * K]の部分集合を作成後、
#   元の配列の部分集合をソートした結果と、ソートした配列の部分集合が一致するかを調べる。
#   O(N log N) + O(K * ceil(N / K) * K log K)

sorted_A = sorted(A)
for i in range(K):
    sub_A1 = sorted([A[j] for j in range(i, N, K)])
    sub_A2 = [sorted_A[j] for j in range(i, N, K)]
    # print(i, sub_A1, sub_A2)
    if sub_A1 != sub_A2:
        print('No')
        sys.exit()
print('Yes')
