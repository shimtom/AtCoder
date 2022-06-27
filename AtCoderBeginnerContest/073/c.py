N = int(input())
A = []
for _ in range(N):
    a = int(input())
    A.append(a)

# A中に奇数個存在する文字の種類を数えればよい
# AをソートすればO(N)で数えることができる。
# 他にも辞書を使うなどすれば解ける？
A = sorted(A)
answer = 0
target = None
count = 0
for i, a in enumerate(A):
    if target == a:
        count += 1
    else:
        if count % 2 == 1:
            answer += 1
        target = a
        count = 1
    # if i + 1 == N and count > 0 and count % 2 == 0:
    #     answer += 1
    if i + 1 == N and count % 2 == 1:
        answer += 1


print(answer)
