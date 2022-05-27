N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = input().split()
    X.append(int(x))
    Y.append(int(y))

# points = [ list(map(int, input().split())) for _ in range(N) ]
# 三角形にならない <-> 3点が直線上にある
# <-> 適当な組みで作った2つのベクトルの内積/大きさが1 or -1
# <-> dx2 * dy1 == dx1 * dy2

# O(N^3)
answer = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            S = (X[k] - X[i]) * (Y[j] - Y[i]) - (X[j] - X[i]) * (Y[k] - Y[i])
            if S != 0:
                answer += 1

print(answer)
