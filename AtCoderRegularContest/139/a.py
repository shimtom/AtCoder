N = int(input())
T = [int(t) for t in input().split()]

# A[i] = 1 << T[i]
# A[i] > A[i - 1]のとき、何もしない
# A[i] <= A[i - 1]のとき
#   T[i - 1] > T[i]のとき、A[i - 1] < A[i]なので A[i] =  (1 << T[i]) + A[i - 1]
#   T[i - 1] <= T[i]のとき
#     A[i] = (1 << T[i])
#   そうでない場合は(1 << T[i])に(i << T[i] + 1) をA[i - 1]を越えるまで加算する

A = []
for i, t in enumerate(T):
    a = 0
    forward = 0
    backward = 1 << t
    if i - 1 >= 0 and backward <= A[i - 1]:
        mask = (1 << t + 1) - 1
        forward = (A[i - 1] >> t + 1)
        if A[i - 1] & mask >= backward:
            forward += 1
        forward <<= t + 1

        # 時間がかかりすぎる
        # while a <= A[i - 1]:
        #     a += 1 << (t + 1)


    a = forward + backward

    A.append(a)

print(A[-1])
