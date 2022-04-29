S = input()

# 幅優先探索
Q = [S]
while len(Q):
    s = Q.pop(0)
    for k in ['dream', 'dreamer', 'erase', 'eraser']:
        if s.startswith(k):
            Q.append(s[len(k) :])
if len(s) == 0:
    print('YES')
else:
    print('NO')
