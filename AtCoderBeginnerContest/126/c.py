import math

N, K = [int(x) for x in input().split()]

# コインの表を出し続けなければいけない回数をxとする
# サイコロn -> n * 2^xがKを超えるとき。つまり、x = ceil(log(K) - log(n))。この時の勝率も1 / N * (1 / 2)^x。
# ただし、1 <= n < Kであり、log()の底は2。
# よって、サイコロの目nが
#   1 <= n < K のとき、1 / N * (1 / 2)^ceil(log(K) - log(n))
#   K <= n < N のとき、1 / N

answer = 0
for n in range(1, min(N, K - 1) + 1):
    # print(i + 1, 1 / (2 ** int(math.ceil(math.log2(K) - math.log2(i + 1)))))
    answer += 1 / (2 ** int(math.ceil(math.log2(K) - math.log2(n))))

answer += max(N - K + 1, 0)
answer /= N

print(answer)
