import sys

N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

eats = []

max_a = max(A)
for i in range(len(A)):
    if A[i] == max_a and i + 1 in B:
        print('Yes')
        sys.exit()

print('No')
