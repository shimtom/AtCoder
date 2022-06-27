N = int(input())
S = input()

# S[i] != S[j] and S[i] != S[k] and S[j] != S[k]なのはS[i], S[j], S[k]に対応する文字がそれぞれ異なるとき。
# なのでこの条件を満たす組み合わせの数は、Sに存在するR,G,Bの数を掛け合わせたもの。
# ただし、j - i != k -j なので全通りから、この条件になる組み合わせを削除すればよい。
# k=2j - i のときに初めの条件を満たした場合を組み合わせの数から引くことで求められる。
# kの探索にi,jを全探索する必要があるのでO(N^2)

R, G, B = 0, 0, 0
for s in S:
    if s == 'R':
        R += 1
    elif s == 'G':
        G += 1
    elif s == 'B':
        B += 1

answer = R * G * B
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        k = 2 * j - i
        if k < N and S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
            answer -= 1

print(answer)
