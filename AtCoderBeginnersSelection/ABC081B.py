N = int(input())
A = [int(a) for a in input().split()]
nums = []

for a in A:
    num = 0
    while a % 2 == 0:
        a = a / 2
        num += 1
    nums.append(num)

print(min(nums))
