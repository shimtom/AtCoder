R, C = [int(x) for x in input().split()]
A = []
for _ in range(2):
    A.append([int(a) for a in input().split()])

print(A[R - 1][C - 1])
