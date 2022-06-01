H, W = [int(x) for x in input().split()]
S = []
for _ in range(H):
    s = input()
    S.append(s)

posis = []
for i in range(H):
    if len(posis) == 2:
        break

    for j in range(W):
        if len(posis) == 2:
            break
        if S[i][j] == 'o':
            posis.append((i, j))

print(abs(posis[0][0] - posis[1][0]) + abs(posis[0][1] - posis[1][1]))
