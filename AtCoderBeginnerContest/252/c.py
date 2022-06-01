N = int(input())
S = []
for _ in range(N):
    S.append(input())

# 0-9の文字、それぞれを揃えた場合に何秒かかるかを求めて最小のものを表示する
answer = 100000000000
time_list = []
for n in range(10):
    n = str(n)
    indices = []
    times = []
    for s in S:
        i = s.index(n)
        c = indices.count(i)
        t = i
        if c > 0:
            t += indices.count(i) * 10
        indices.append(i)
        times.append(t)
    time_list.append(max(times))

print(min(time_list))
