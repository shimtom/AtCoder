N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

memo = set()
answer = 0
for a in A:
    if a in memo:
        answer += 1
    else:
        memo.add(a)

print(answer)
