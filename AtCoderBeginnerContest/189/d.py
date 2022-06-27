N = int(input())
S = []
for _ in range(N):
    S.append(input())

# 単純にシミュレーションするとO(2^N)
# 回答をf(S[1], ..., S[N])とすると、
# S[N]がOR: f(S[1], ..., S[N]) = 2^N + f(S[1], ..., S[N - 1])
#   右辺がFalseであれば、f(S[1], ..., S[N - 1])
#   右辺がTrueであれば、左辺はなんでもよいので 2^N
# S[N]がAND: f(S[1], ..., S[N]) = f(S[1], ..., S[N - 1])
#   右辺がFalseであれば、左辺に何がきても0
#   左辺がTrueであれば、左辺に依存するのでF(S[1], ..., S[N - 1])
# ただし、f() = 1
#
# 以上より、S[N]からS[1]の順番でf()を展開していけばよい

answer = 0
for i, s in reversed(list(enumerate(S))):
    if s == 'OR':
        answer += 2 ** (i + 1)
    if i == 0:
        answer += 1

print(answer)
