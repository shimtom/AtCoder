import sys

L, R = [int(x) for x in input().split()]

answer = 2020
for i in range(L, R):
    for j in range(i + 1, R + 1):
        mod = (i * j) % 2019
        answer = min(answer, mod)

        if answer == 0:
            print(answer)
            sys.exit()
else:
    print(answer)
