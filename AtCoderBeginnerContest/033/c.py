S = input()

# 数字を0に書き換えて答えを0にするには、式を加算項に分割し、各項が0になるように書き換えればよい。
# 乗算項は値のどれか一つを0にすればよい。
# O(N)

answer = 0
num = 1
for ss in S.split('+'):
    num = 1
    for i, s in enumerate(ss):
        if i == 0:
            num = int(s)
        elif s != '*':
            num *= int(s)
    if num != 0:
        answer += 1

print(answer)
