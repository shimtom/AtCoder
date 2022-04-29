N, A, B = [int(v) for v in input().split()]

nums = []
for n in range(N):
    n = n + 1
    s = sum([int(v) for v in str(n)])
    if A <= s <= B:
        nums.append(n)

print(sum(nums))
