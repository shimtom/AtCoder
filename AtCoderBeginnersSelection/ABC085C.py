N, Y = [int(v) for v in input().split()]


def ans():
    for a in range(1 + N):
        for b in range(1 + N - a):
            c = max(N - a - b, 0)
            if 10000 * a + 5000 * b + 1000 * c == Y:
                return a, b, c
    return -1, -1, -1


print(*ans())
