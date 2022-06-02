N = int(input())
A = [int(a) for a in input().split()]

for i, a in sorted([(i, a) for i, a in enumerate(A)], key=lambda ia: ia[1], reverse=True):
    print(i + 1)
