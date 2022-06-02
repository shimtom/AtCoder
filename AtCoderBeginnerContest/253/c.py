Q = int(input())
queries = []
for _ in range(Q):
    q = [int(x) for x in input().split()]
    queries.append(q)

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
        x, c = q[1], q[2]
        S[x] = S.get(x, 0) - min(c, S.get(x, 0))
        if S[x] == 0:
            S.pop(x, None)
            if len(S.keys()) > 0:
                if min_value == x:
                    min_value = min(S.keys())
                if max_value == x:
                    max_value = max(S.keys())
    elif q[0] == 3:
        print(max_value - min_value)
