N = int(input())


summation = sum([(i + 1) * (j + 1) for i in range(9) for j in range(9)])
diff = summation - N
for i in range(9):
    mod = diff % (i + 1)
    quotient = diff // (i + 1)

    if mod == 0 and 1 <= quotient <= 9:
        print('{} x {}'.format(i + 1, quotient))
