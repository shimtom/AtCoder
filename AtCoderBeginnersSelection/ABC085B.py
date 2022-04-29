N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))
d = sorted(d, reverse=True)

n = 0
before = 101
for v in d:
    if v < before:
        n += 1
        before = v
print(n)
