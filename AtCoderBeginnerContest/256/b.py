N = int(input())
A = list(map(int, input().split()))

answer = 0

mass = [0] * 4
for a in A:
    mass[0] += 1

    for i, x in reversed(list(enumerate(mass))):
        if i + a >= len(mass) :
            answer += x
        else:
            mass[i + a] = x
        mass[i] = 0

print(answer)
