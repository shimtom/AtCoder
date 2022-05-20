N, A, B = [int(x) for x in input().split()]
answer = [['x' for _ in range(B * N)] for _ in range(A * N)]


for i in range(N):
    if (i - 1) * A < 0 or answer[(i - 1) * A][0] == '#':
        tile = '.'
    else:
        tile = '#'
    for j in range(N):
        # if current == '.':
        for y in range(i * A, (i + 1) * A):
            for x in range(j * B, (j + 1) * B):
                answer[y][x] = tile
        if tile == '.':
            tile = '#'
        else:
            tile = '.'

for line in answer:
    print(''.join(line))
