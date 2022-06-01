a, b, c = [int(x) for x in input().split()]

if sorted([a, b, c])[1] == b:
    print('Yes')
else:
    print('No')
