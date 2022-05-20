H, W = [int(x) for x in input().split()]
R, C = [int(x) for x in input().split()]

answer = 0
if 0 < R - 1 <= H:
    answer += 1
if 0 < R + 1 <= H:
    answer += 1
if 0 < C - 1 <= W:
    answer += 1
if 0 < C + 1 <= W:
    answer += 1

print(answer)
