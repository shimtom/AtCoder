N, X = [int(x) for x in input().split()]

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = ''.join([a * N for a in alphabets])[X - 1]

print(answer)
