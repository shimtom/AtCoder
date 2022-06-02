N = 3
S = []
for _ in range(N):
    S.append(input())

indices = [0] * N
current = 0
while indices[current] < len(S[current]):
    x = S[current][indices[current]]
    indices[current] += 1

    if x == 'a':
        current = 0
    elif x == 'b':
        current = 1
    elif x == 'c':
        current = 2


if current == 0:
    print('A')
elif current == 1:
    print('B')
elif current == 2:
    print('C')
