N = int(input())
P = []
for _ in range(N):
    t, x, y = [int(v) for v in input().split()]
    P.append((t, x, y))


# 深さ優先: TL
# ans = 'No'
# S = [((0, 0, 0), P)]
# while len(S):
#     (t, x, y), p = S.pop()
#     if len(p) == 0:
#         ans = 'Yes'
#         break

#     pt, px, py = p[0]
#     if pt - t < abs(px - x) + abs(py - y):
#         continue
#     if t < pt:
#         S.append(((t + 1, x + 1, y), p))
#         S.append(((t + 1, x - 1, y), p))
#         S.append(((t + 1, x, y + 1), p))
#         S.append(((t + 1, x, y - 1), p))
#         continue
#     if t == pt and x == px and y == py:
#         S.append(((t + 1, x + 1, y), p[1:]))
#         S.append(((t + 1, x - 1, y), p[1:]))
#         S.append(((t + 1, x, y + 1), p[1:]))
#         S.append(((t + 1, x, y - 1), p[1:]))
ans = 'Yes'
t, x, y = 0, 0, 0
for pt, px, py in P:
    dt = pt - t
    d = abs(px - x) + abs(py - y)
    if d > dt:
        ans = 'No'
        break
    else:
        if (dt - d) % 2 == 1:
            ans = 'No'
            break

# (t, x, y), dt, dx + dy
# dx + dy > dt: False
# dx + dy <= dt
#   dx + dy == dt ok
#   dx + dy < dt
#     (dt - (dx + dy) )  % 2 == 0
# dx + dy - 2 == dt ok

print(ans)
