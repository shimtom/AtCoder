import sys

N = int(input())
names = [input().split() for _ in range(N)]

for i in range(N):
    last_ok, first_ok = True, True
    last, first = names[i]

    # wrong code
    # for j in range(i + 1, N):

    for j in range(N):
        if i == j:
            continue

        if last == names[j][0] or last == names[j][1]:
            last_ok = False
        if first == names[j][0] or first == names[j][1]:
            first_ok = False

    if not last_ok and not first_ok:
        print('No')
        sys.exit()

print('Yes')
