from math import sqrt

A, B = input().split()
A = int(A)
B = int(B)

d = A ** 2 + B ** 2
x = A / sqrt(d)
y = B / sqrt(d)

print(x, y)
