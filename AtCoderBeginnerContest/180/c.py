import math

N = int(input())

# 約数を全て求めればよい

answer = []
for i in range(int(math.sqrt(N))):
    if N % (i + 1) == 0:
        answer.append(i + 1)
        if i + 1 != N // (i + 1):
            answer.append(N // (i + 1))

for a in sorted(answer):
    print(a)
