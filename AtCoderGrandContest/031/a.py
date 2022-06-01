N = int(input())
S = input()

nums = [0 for _ in range(26)]
for s in S:
    nums[ord(s) - ord('a')] += 1

ans = 1
for n in nums:
    ans = ans * (n + 1)
ans -= 1
ans %= 1000_000_007
print(ans)
