N, K = [int(x) for x in input().split()]
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]

# X = []
X = [True, True, True, True]
for i in range(N - 1):
    x_aa, x_ab, x_ba, x_bb = X
    # if i == 0:
    #     x_aa, x_ab, x_ba, x_bb = True, True, True, True
    # else:
    #     x_aa, x_ab, x_ba, x_bb = X[i - 1]

    X = [
        (x_aa or x_ba) and abs(A[i + 1] - A[i]) <= K,
        (x_aa or x_ba) and abs(B[i + 1] - A[i]) <= K,
        (x_ab or x_bb) and abs(A[i + 1] - B[i]) <= K,
        (x_ab or x_bb) and abs(B[i + 1] - B[i]) <= K,
    ]
    # X.append(x)

for x in X:
    if x:
        print('Yes')
        break
else:
    print('No')


# stack = [(0, A[0]), (0, B[0])]
# while len(stack):
#     i, x = stack.pop()
#     if i + 1 == N:
#         print('Yes')
#         break

#     if abs(A[i + 1] - x) <= K:
#         stack.append((i + 1, A[i + 1]))
#     if abs(B[i + 1] - x) <= K:
#         stack.append((i + 1, B[i + 1]))
# else:
#     print('No')

# X = []
# for x in A + B:
#     if x not in X:
#         X.append(x)

# X = sorted(X)

# i = 0
# s = 0
# while i < len(X) - 1:
#     if abs(X[i] - X[i + 1]) > K:
#         if i - s + 1 >= N:
#             print('Yes')
#             break
#         else:
#             s = i

#     i += 1
# else:
#     if i - s + 1 >= N:
#         print('Yes')
#     else:
#         print('No')
