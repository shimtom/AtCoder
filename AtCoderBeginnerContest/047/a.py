a, b, c = [int(x) for x in input().split()]

packs = sorted([a, b, c])

if packs[0] + packs[1] == packs[2]:
    print('Yes')
else:
    print('No')
