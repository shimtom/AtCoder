A, B = input().split()
A = int(A)
B1, B2 = B.split('.')
B = int(B1) * 100 + int(B2)

answer = (A * B) // 100

print(answer)
