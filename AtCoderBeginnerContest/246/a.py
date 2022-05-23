xs = []
ys = []

for _ in range(3):
    x, y = input().split()
    xs.append(int(x))
    ys.append(int(y))


for x in xs:
    if xs.count(x) == 1:
        break

for y in ys:
    if ys.count(y) == 1:
        break

print(x, y)
