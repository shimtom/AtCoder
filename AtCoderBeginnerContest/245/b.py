N = int(input())
A = [int(a) for a in input().split()]

ans = 0
for a in sorted(A):
    if a == ans:
        ans += 1

print(ans)
