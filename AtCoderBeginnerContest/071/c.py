N = int(input())
A = [int(a) for a in input().split()]

# 長方形を作成するためには同じ長さの棒が2本ずつ必要
# 棒の数を数え、短辺、長辺に使用できるかを確認しつつ短辺、長辺を更新する
# O(N + N) = O(N)

counts = dict()
for a in A:
    counts[a] = counts.get(a, 0) + 1

short, long = 0, 0
for k, v in counts.items():
    for _ in range(min(2, v // 2)):
        if k > long:
            short = long
            long = k
        elif k > short:
            short = k

print(short * long)
