N, Q = [int(x) for x in input().split()]
X = [int(input()) for _ in range(Q)]

A = [i + 1 for i in range(N)]

# O(Q)
indices = [i - 1 for i in range(N + 1)]
for x in X:
    i = indices[x]
    j = i + 1 if i + 1 < len(A) else i - 1

    a = A[i]
    b = A[j]

    # swap
    A[j] = a
    A[i] = b

    # memory indices
    indices[a] = j
    indices[b] = i


# O(N x Q)
# for x in X:
#     i = A.index(x)
#     if i + 1 < len(A):
#         j = i + 1
#     else:
#         j = i -1
#
#     A[i], A[j] = A[j], A[i]

# print answer
print(' '.join(str(a) for a in A))
