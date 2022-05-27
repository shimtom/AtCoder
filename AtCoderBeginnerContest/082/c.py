N = int(input())
A = [int(a) for a in input().split()]

keys = set(A)
counts = {a: 0 for a in keys}
for a in A:
    counts[a] += 1

answer = 0
for a in keys:
    if counts[a] > a:
        answer += counts[a] - a
    elif counts[a] < a:
        answer += counts[a]

print(answer)
