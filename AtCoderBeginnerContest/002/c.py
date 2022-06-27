xa, ya, xb, yb, xc, yc = [int(x) for x in input().split()]

S = abs((xa - xc) * (yb - yc) - (xb - xc) * (ya - yc)) / 2
print(S)
