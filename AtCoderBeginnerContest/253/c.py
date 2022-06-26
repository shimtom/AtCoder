Q = int(input())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

S = dict()
min_value = 10 ** 9 + 1
max_value = -1
for q in queries:
    if q[0] == 1:
        x = q[1]
        S[x] = S.get(x, 0) + 1
        min_value = min(min_value, x)
        max_value = max(max_value, x)
    elif q[0] == 2:
        x = q[1]
        c = q[2]
        S[x] = S.get(x, 0) - min(S.get(x, 0), c)
        if S[x] == 0:
            S.pop(x, None)
            if min_value == x:
                if len(S) > 0:
                    min_value = min(S.keys())
                else:
                    min_value = 10 ** 9 + 1
            if max_value == x:
                if len(S) > 0:
                    max_value = max(S.keys())
                else:
                    max_value = -1
    elif q[0] == 3:
        print(max_value - min_value)
