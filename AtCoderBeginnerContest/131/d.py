import sys

N = int(input())
JOBS = []
for _ in range(N):
    a, b = input().split()
    JOBS.append((int(a), int(b)))

JOBS = sorted(JOBS, key=lambda ab: ab[1])

elapsed_time = 0
for a, b in JOBS:
    elapsed_time += a

    if elapsed_time > b:
        print('No')
        sys.exit()

print('Yes')
