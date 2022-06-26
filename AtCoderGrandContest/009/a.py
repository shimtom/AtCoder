N = int(input())
A = []
B = []
for _ in range(N):
    a, b = input().split()
    A.append(int(a))
    B.append(int(b))

# 3 5: (3 % 5) - 5 = -2
# 2 7:  (2 % 7) - 7 = -5 -> -2
# 9 4:  (9 % 4) - 4 = -3 -> 3

total_count = 0
for i in reversed(range(N)):
    current = A[i] + total_count
    need_count = 0
    if current % B[i] > 0:
        need_count = abs(current % B[i] - B[i])
    total_count += need_count
    # total_count += abs((A[i] + total_count) % B[i] - B[i])

print(total_count)
